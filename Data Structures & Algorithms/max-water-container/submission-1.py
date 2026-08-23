class Solution:
    def maxArea(self, heights: List[int]) -> int:
        maximum = 0
        length = len(heights)
        l, r = 0,  length - 1

        while l < r:
            water = min(heights[l], heights[r]) * (r - l)
            maximum = max(water, maximum)
            if heights[l] <= heights[r]:
                l += 1
            elif heights[l] > heights[r]:
                r -= 1
        return maximum