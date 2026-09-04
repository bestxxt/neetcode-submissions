import math

class Solution:
    def eat(self, piles: List[int], k):
        h = 0
        for p in piles:
            h += math.ceil(p / k)
        return h

    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        hi = max(piles)
        lo = 1
        while lo <= hi:
            mid = (lo + hi) // 2
            k = self.eat(piles, mid)
            if k > h:
                lo = mid +1
            elif k <= h:
                hi = mid -1

        return lo
            