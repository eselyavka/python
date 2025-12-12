import heapq
import unittest


class Solution(object):
    def countMentions(self, numberOfUsers, events):
        """
        :type numberOfUsers: int
        :type events: List[List[str]]
        :rtype: List[int]
        """
        users = {"id{0}".format(uid): uid for uid in range(numberOfUsers)}
        ans = [0] * numberOfUsers
        online = [True] * numberOfUsers
        heap = []
        events.sort(key=lambda t: (int(t[1]), -1 if t[0] == "OFFLINE" else 1))

        for event in events:
            msg, curr_ts, ids = event
            if msg == "OFFLINE":
                heapq.heappush(heap, (int(curr_ts) + 60, int(ids)))
                online[int(ids)] = False
                continue

            while heap and heap[0][0] <= int(curr_ts):
                exp_ts, uid = heapq.heappop(heap)
                online[uid] = True

            for _, uid in heap:
                online[uid] = False

            if ids in ["ALL", "HERE"]:
                ans = [i + 1 for i in ans] if ids == "ALL" else [i + (1 if online[uid] else 0) for uid, i in
                                                                 enumerate(ans)]
                continue

            for i in ids.split():
                user = i.strip()
                user_id = users[user]
                ans[user_id] += 1

        return ans


class TestSolution(unittest.TestCase):
    def test_countMentions(self):
        solution = Solution()
        self.assertEqual(solution.countMentions(3, [["MESSAGE", "1", "ALL"], ["OFFLINE", "66", "1"],
                                                    ["MESSAGE", "66", "HERE"], ["OFFLINE", "5", "1"]]), [2, 1, 2])


if __name__ == '__main__':
    unittest.main()
