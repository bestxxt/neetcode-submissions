class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums_sorted = sorted(nums)
        n = len(nums_sorted)

        for i in range(n - 2):
            if nums_sorted[i] > 0:
                break
            if i > 0 and nums_sorted[i] == nums_sorted[i - 1]:
                continue 

            target = - nums_sorted[i]
            p1, p2 = i + 1, n - 1              

            while p1 < p2:
                s = nums_sorted[p1] + nums_sorted[p2]
                if s > target:
                    p2 -= 1
                elif s < target:
                    p1 += 1
                else:
                    res.append([nums_sorted[i], nums_sorted[p1], nums_sorted[p2]])
                    p1 += 1
                    p2 -= 1         
                    while p1 < p2 and nums_sorted[p1] == nums_sorted[p1 - 1]:
                        p1 += 1
                    while p1 < p2 and nums_sorted[p2] == nums_sorted[p2 + 1]:
                        p2 -= 1
        return res
