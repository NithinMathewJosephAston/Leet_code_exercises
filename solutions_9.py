class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        cnt = 0
        tmp = len(nums)
        for i in range(len(nums)):
            if val == nums[i]:
                nums.pop(i)
                nums.append(0)
                cnt += 1
        length = len(nums) - cnt
        return length


gems = Solution()
print(gems.removeElement([3,2,2,3], 3))