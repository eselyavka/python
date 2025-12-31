from collections import deque, defaultdict


def rps(raw_logs, window_size):
    if not raw_logs or window_size <= 0:
        return {}

    parsed = []
    for line in raw_logs:
        ts_s, endpoint, _ = line.split()
        parsed.append((int(ts_s), endpoint))

    parsed.sort(key=lambda x: x[0])

    window = deque()
    counter = defaultdict(int)
    max_count = defaultdict(int)

    for ts, endpoint in parsed:
        window.append((ts, endpoint))
        counter[endpoint] += 1
        max_count[endpoint] = max(max_count.get(endpoint, 0), counter[endpoint])
        while window and ts - window[0][0] >= window_size:
            old_ts, old_endpoint = window.popleft()
            counter[old_endpoint] -= 1

    return {ep: f"{float(max_count[ep]) / float(window_size):.2f}" for ep in max_count.keys()}


if __name__ == "__main__":
    logs = [
        "100 /api/user 200",
        "101 /api/user 200",
        "102 /api/user 500",
        "103 /api/order 200",
        "104 /api/user 200",
        "105 /api/order 500",
        "106 /api/user 200",
        "107 /api/order 200",
    ]
    window_size = 3

    res = rps(logs, window_size)

    assert res == {"/api/user": "1.00", "/api/order": "0.67"}
