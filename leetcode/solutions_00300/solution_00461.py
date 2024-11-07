class Solution461(object):
    def hamming_distance(self, x, y):
        """
        :type x: int
        :type y: int
        :rtype: int
        """
        distance = 0
        for b in bin(x ^ y)[2:]:
            if int(b) & 1:
                distance += 1
        return distance
