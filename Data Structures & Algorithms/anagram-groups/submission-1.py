class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        strs_sorted = {}
        for s in strs:
            tmp = ''.join(sorted(s))
            if tmp not in strs_sorted:
                strs_sorted[tmp] = []
            strs_sorted[tmp].append(s)
    
        return list(strs_sorted.values())