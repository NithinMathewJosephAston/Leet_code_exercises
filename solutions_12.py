class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        numbers = map(lambda x: str(x), digits)
        value = str(eval(''.join(numbers))+1)
        value_ = [int(i) for i in value]
        return value_
gems = Solution()
print(gems.plusOne([1,1]))