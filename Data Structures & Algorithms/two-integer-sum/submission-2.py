class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            n = target - nums[i]
            if n in nums and i != nums.index(n):
                j = nums.index(target - nums[i])
                return sorted([i,j])
        return False