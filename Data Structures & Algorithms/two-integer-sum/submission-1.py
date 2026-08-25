class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            if target - nums[i] in nums:
                j = nums.index(target - nums[i])
                return sorted([i,j])
        return False