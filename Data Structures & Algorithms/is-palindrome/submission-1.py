import re

class Solution:
    def isPalindrome(self, s: str) -> bool:
        s_cleaned = re.sub(r'[^a-zA-Z0-9]', '', s).lower()
        print(s_cleaned)
        left = 0
        right = len(s_cleaned) - 1
        
        while left <= right :
            if s_cleaned[left] != s_cleaned[right]:
                return False
            left +=1
            right -=1
        return True
        