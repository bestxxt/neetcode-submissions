class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s2 = sorted(set(s))
        t2 = sorted(set(t))

        if s2 == t2:
            return True
        
        return False

        