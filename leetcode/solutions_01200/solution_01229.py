import unittest


class Solution(object):
    def minAvailableDuration(self, slots1, slots2, duration):
        """
        :type slots1: List[List[int]]
        :type slots2: List[List[int]]
        :type duration: int
        :rtype: List[int]
        """

        slots1.sort(key=lambda x: x[0])
        slots2.sort(key=lambda x: x[0])

        s1, s2 = len(slots1), len(slots2)
        p1, p2 = 0, 0

        while p1 < s1 and p2 < s2:
            start1, start2 = slots1[p1][0], slots2[p2][0]
            end1, end2 = slots1[p1][1], slots2[p2][1]
            diff = min(end1, end2) - max(start1, start2)
            if diff >= duration:
                return [max(start1, start2), max(start1, start2) + duration]

            if end1 < end2:
                p1 += 1
            else:
                p2 += 1

        return []


class TestSolution(unittest.TestCase):
    def test_minAvailableDuration(self):
        solution = Solution()
        self.assertListEqual(solution.minAvailableDuration([[10, 50], [60, 120], [140, 210]],
                                                           [[0, 15], [60, 70]],
                                                           8),
                             [60, 68])


if __name__ == '__main__':
    unittest.main()
