import unittest
from collections import defaultdict
from heapq import heappush, heappop


class Solution(object):
    def mostPopularCreator(self, creators, ids, views):
        """
        :type creators: List[str]
        :type ids: List[str]
        :type views: List[int]
        :rtype: List[List[str]]
        """
        max_dict = {}
        idx_mapping = defaultdict(list)
        for idx, name in enumerate(creators):
            if name in max_dict:
                max_dict[name] += views[idx]
            else:
                max_dict[name] = views[idx]

            idx_mapping[name].append(idx)

        h = []
        for name, cnt in max_dict.items():
            heappush(h, (-cnt, name))

        largest = -1
        names = []
        while h:
            cnt, name = heappop(h)
            if largest > -cnt:
                break
            largest = -cnt
            names.append(name)
        ans = []

        for name in names:
            mapping = idx_mapping[name]
            video_pop = views[mapping[0]]
            video_name = ids[mapping[0]]
            for i in range(1, len(mapping)):
                idx = mapping[i]
                if views[idx] >= video_pop:
                    video_name = min(video_name, ids[idx]) if views[idx] == video_pop else ids[idx]
                    video_pop = views[idx]

            ans.append([name, video_name])
        return ans


class TestSolution(unittest.TestCase):
    def test_mostPopularCreator(self):
        solution = Solution()
        self.assertListEqual(
            solution.mostPopularCreator(["alice", "bob", "alice", "chris"], ["one", "two", "three", "four"],
                                        [5, 10, 5, 4]), [["alice", "one"], ["bob", "two"]])


if __name__ == '__main__':
    unittest.main()
