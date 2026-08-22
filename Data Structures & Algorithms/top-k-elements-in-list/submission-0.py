from collections import defaultdict

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = defaultdict(int)
        ret = []

        for n in nums:
            count[n] += 1

        for i in range(k):
            max_num = None
            max_freq = -1
            for num,freq in count.items():
                if freq > max_freq:
                    max_freq = freq
                    max_num = num
            ret.append(max_num)
            del count[max_num]
            
        return ret
