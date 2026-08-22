from collections import defaultdict

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        count = defaultdict(int)

        for chat in s:
            count[chat] += 1
    
        for chat in t:
            count[chat] -= 1
        
        return all(c == 0 for c in count.values())

            
