import math
from collections import defaultdict
from dataclasses import dataclass


@dataclass(frozen=True)
class EventType:
    SPEEDING: str = "speeding"
    BRAKE: str = "harsh_brake"
    IDLE: str = "idle"


@dataclass(frozen=True)
class Weights:
    SPEED_10_20: int = 3
    SPEED_GT_20: int = 7
    BRAKE_GT_5: int = 5
    IDLE_PER_MIN: int = 1
    MAX: int = 100
    MIN: int = 0


class Rule:
    def score(self, e):
        return 0


class SpeedingRule(Rule):
    def score(self, e):
        if e.get("type", "undef") != EventType.SPEEDING:
            return 0

        v = e.get("value")

        if 10 < v <= 20:
            return Weights.SPEED_10_20
        if v > 20:
            return Weights.SPEED_GT_20

        return 0


class BreakRule(Rule):
    def score(self, e):
        if e.get("type", "undef") != EventType.BRAKE:
            return 0

        v = e.get("value", 0)

        if v > 5:
            return Weights.BRAKE_GT_5

        return 0


class IdleRule(Rule):
    def score(self, e):
        if e.get("type", "undef") != EventType.IDLE:
            return 0

        v = e.get("value", 0)

        if v > 300:
            return v // Weights.IDLE_PER_MIN

        return 0


def risk_score(events, rules=None, lo=0, hi=100):
    rules = rules or [SpeedingRule(), BreakRule(), IdleRule()]
    score = sum([sum([r.score(e) for e in events]) for r in rules])

    return min(max(score, lo), hi)


def segment_trips(points, stop_speed=1.0, stop_seconds=300):
    """
    points: list[dict] sorted by timestamp, each {"ts": int, "speed_kph": float}
    return: list[dict] segments [{"type": "stop"|"drive", "start_ts": int, "end_ts": int}]
    """
    if not points:
        return []

    curr_start = points[0]["ts"]
    below_start = None
    in_stop = False
    below_dur = 0

    ans = []

    for i in range(len(points) - 1):
        p = points[i]
        q = points[i + 1]
        interval = q["ts"] - p["ts"]

        if p["speed_kph"] < stop_speed:
            if below_start is None:
                below_start = p["ts"]
            below_dur += interval
            if not in_stop and below_dur >= stop_seconds:
                ans.append({"type": "drive", "start_ts": curr_start, "end_ts": below_start})
                curr_start = below_start
                in_stop = True
        else:
            if in_stop:
                ans.append({"type": "stop", "start_ts": curr_start, "end_ts": p["ts"]})
                curr_start = p["ts"]
                in_stop = False
            below_start = None
            below_dur = 0

    last_ts = points[-1]["ts"]
    if in_stop:
        ans.append({"type": "stop", "start_ts": curr_start, "end_ts": last_ts})
    else:
        ans.append({"type": "drive", "start_ts": curr_start, "end_ts": last_ts})

    return ans


def haversine_m(lat1, lon1, lat2, lon2):
    R = 6371000.0
    p1, p2 = math.radians(lat1), math.radians(lat2)
    dphi = math.radians(lat2 - lat1)
    dlambda = math.radians(lon2 - lon1)
    a = math.sin(dphi / 2) ** 2 + math.cos(p1) * math.cos(p2) * math.sin(dlambda / 2) ** 2
    return 2 * R * math.asin(math.sqrt(a))


def dejitter(points, min_move_m=5.0):
    """
    points: [{"ts": int, "lat": float, "lon": float}, ...] sorted by ts
    return: filtered list keeping first point and any point >= min_move_m from last kept
    """
    first = points[0]
    ans = [first]

    for p in points[1:]:
        f_lat, f_lon = first["lat"], first["lon"]
        p_lat, p_lon = p["lat"], p["lon"]
        distance = haversine_m(f_lat, f_lon, p_lat, p_lon)
        if distance > min_move_m:
            first = p
            ans.append(p)
    return ans


def idle_seconds_by_vehicle(events):
    """
    events: list[dict] ordered by ts
    return: dict {vehicle_id: total_idle_seconds}
    """
    ans = defaultdict(int)
    acc = defaultdict(list)
    for e in events:
        vehicle_id = e["vehicle_id"]
        if e["event"] == "idle_end":
            item = acc.get(vehicle_id)
            if item is not None:
                duration = e["ts"] - item
                ans[vehicle_id] += duration
                acc.pop(vehicle_id)
        else:
            acc[vehicle_id] = e["ts"]

    last = events[-1]["ts"]
    if acc:
        for v_id, ts in acc.items():
            duration = last - ts
            ans[v_id] += duration

    return ans


if __name__ == "__main__":
    data = [
        {"ts": 0, "speed_kph": 30.0},
        {"ts": 60, "speed_kph": 28.0},
        {"ts": 120, "speed_kph": 0.5},
        {"ts": 240, "speed_kph": 0.2},
        {"ts": 360, "speed_kph": 0.0},
        {"ts": 480, "speed_kph": 0.0},  # now 6 min below 1.0 -> a stop
        {"ts": 600, "speed_kph": 10.0},
        {"ts": 660, "speed_kph": 20.0},
    ]
    print(segment_trips(data))

    pts = [
        {"ts": 0, "lat": 43.0, "lon": -79.0},
        {"ts": 5, "lat": 43.00001, "lon": -79.0},
        {"ts": 10, "lat": 43.00020, "lon": -79.0},  # ~22m -> keep
    ]

    print(dejitter(pts, 5.0))

    events = [
        {"vehicle_id": "A", "event": "idle_start", "ts": 0},
        {"vehicle_id": "B", "event": "idle_start", "ts": 10},
        {"vehicle_id": "A", "event": "idle_end", "ts": 70},  # A idle 70
        {"vehicle_id": "B", "event": "idle_end", "ts": 100},  # B idle 90
        {"vehicle_id": "A", "event": "idle_start", "ts": 120},
        {"vehicle_id": "C", "event": "idle_end", "ts": 200},
        # stream ends at 200; A still idling -> count 80
    ]
    print(idle_seconds_by_vehicle(events))
