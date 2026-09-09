class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # Finding the jumper
        lo, hi = 0, len(nums) - 1
        while lo < hi:
            # print([lo,hi])
            mid = (lo + hi) // 2
            if nums[mid] > nums[lo]:
                lo = mid 
            else:
                hi = mid - 1
        if target >= nums[0] and target <= nums[lo]:
            for i in range(lo+1):
                print(i)
                if nums[i] == target:
                    return i
            return -1
        else:
            for i in range(lo,len(nums)):
                if nums[i] == target:
                    return i
            return -1

        return -1
                

        


