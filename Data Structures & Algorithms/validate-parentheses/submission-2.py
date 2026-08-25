class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for c in s:
            if c in ['(', '{', '[']:
                stack.append(c)
            else:
                if len(stack) > 0:
                    tmp = stack.pop()
                else:
                    return False
                
                if tmp == "(" and c != ")":
                    return False
                if tmp == "{" and c != "}":
                    return False
                if tmp == "[" and c != "]":
                    return False
        if len(stack) > 0:
            return False
        return True
