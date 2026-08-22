class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        output = []

        # left -> right
        l2r = []
        tmp = 1
        for num in nums:
            tmp *= num
            l2r.append(tmp)

        # right -> left
        r2l = []
        tmp = 1
        for num in nums[::-1]:
            tmp *= num
            r2l.append(tmp)
            
        r2l = r2l[::-1]

        for i, num in enumerate(nums):
            n = len(nums)
            left = l2r[i-1] if i > 0 else 1
            right = r2l[i+1] if i < n - 1 else 1
            output.append(left * right)

        return output