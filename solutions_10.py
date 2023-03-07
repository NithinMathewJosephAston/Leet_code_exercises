class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        val = 0
        if target in nums:
            val = nums.index(target)
        else:
            for index in range(len(nums)):
                if nums[index] < target and index + 1 > len(nums)-1:
                    val = index + 1
                elif nums[index] < target < nums[index+1]:
                    val = index + 1
        return val

gems = Solution()
print(gems.searchInsert([1,3,5,6], 7))