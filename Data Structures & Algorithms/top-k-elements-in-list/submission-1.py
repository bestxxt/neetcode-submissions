class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        for num in nums:
            count[num] = count.get(num, 0) + 1
        
        buckets = [[] for _ in range(len(nums)+1)]

        for num, freq in count.items():
            buckets[freq].append(num)

        # buckets[0] = [1,2,3]
        # buckets[1] = [4,5]
        ret = []
        for freq in range(len(buckets) - 1, 0, -1):
            for num in buckets[freq]:
                ret.append(num)
                if len(ret) == k:
                    return ret
        return ret
