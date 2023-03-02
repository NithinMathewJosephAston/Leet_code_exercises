class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        two_sum = []
        for index in range(len(nums)):
            for rest in range(index+1, len(nums)):
                if target == nums[index]+nums[rest]:
                    return [index, rest]


gems = Solution()
print(gems.twoSum([3,2,4], 6))