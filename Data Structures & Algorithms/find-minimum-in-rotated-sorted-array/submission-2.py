class Solution:
    def findMin(self, nums: List[int]) -> int:
        if nums[0] <= nums[-1]:
            return nums[0]
        
        # find the jumper
        lo = 0
        hi = len(nums) - 1

        while lo <= hi:
            mid = (lo + hi) // 2
            if nums[mid] == nums[lo]:
                # print('f')
                return nums[mid+1]
            elif nums[mid] < nums[lo]:
                hi = mid 
            elif nums[mid] > nums[lo]:
                lo = mid 
        return nums[hi]