class Solution(object):
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        a_ = int(a, 2)
        b_ = int(b, 2)
        c = a_ + b_
        return bin(c)[2:]

gems = Solution()
print(gems.addBinary('1010', '1011'))