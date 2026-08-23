class Solution:
    def trap(self, height: List[int]) -> int:
        # left maximum
        maximum = 0
        l_max = []
        for h in range(0, len(height)):
            l_max.append(maximum)
            maximum = max(height[h], maximum)

        # right maximum
        maximum = 0
        r_max = []
        for h in range(len(height) - 1, -1, -1):
            r_max.append(maximum)
            maximum = max(height[h], maximum)
        
        r_max = r_max[::-1]
        # print(l_max, r_max)
        
        w = 0
        for i in range(len(l_max)):
            tmp = min(l_max[i], r_max[i]) - height[i]
            tmp = max(tmp, 0)
            w += tmp

        return w