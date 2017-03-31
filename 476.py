class Solution(object):
    def findComplement(self, num):
        """
        :type num: int
        :rtype: int
        """
        sum = 0
        tmp = num
        while (num > 0) :
            sum = (sum << 1) + 1
            num = num >> 1
        return sum - tmp

print(Solution().findComplement(5))
print(Solution().findComplement(2))
print(Solution().findComplement(1))