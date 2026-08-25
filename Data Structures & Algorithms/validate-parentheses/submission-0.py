class Solution:
    def isValid(self, s: str) -> bool:
        stack = []

        for c in s:
            if c in ['(', '{', '[']:
                stack.append(c)
            else:
                tmp = stack.pop()
                if c == ')' and tmp != "(":
                    return False
                if c == ']' and tmp != "[":
                    return False
                if c == '}' and tmp != "{":
                    return False
        return True