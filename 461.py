class Solution(object):
    def hammingDistance(self, x, y):
        """
        :type x: int
        :type y: int
        :rtype: int
        """
        z = x ^ y
        cnt = 0
        while (z > 0) :
            z &= z - 1
            cnt += 1
        return cnt
