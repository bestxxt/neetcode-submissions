class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        count_h = {}
        for s in strs:
            count = [0] * 26
            for letter in s:
                count[ord(letter) - ord('a')] += 1
            if tuple(count) not in count_h:
                count_h[tuple(count)] = []
            count_h[tuple(count)].append(s)
        return list(count_h.values())


