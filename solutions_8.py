class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        length = len(nums)
        tmp = None
        cnt = 0
        for i in range(length):
            if nums[i] != tmp:
                tmp = nums[i]
                nums[cnt] = nums[i]
                cnt += 1
        return cnt

gems = Solution()
print(gems.removeDuplicates([1,1,2]))