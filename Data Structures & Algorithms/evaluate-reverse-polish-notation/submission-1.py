class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for t in tokens:
            if t in ["+", "-", "*", "/"]:
                # branch 1
                r = int(stack.pop())
                l = int(stack.pop())
                if t == "+": res = l + r
                if t == "-": res = l - r
                if t == "*": res = l * r
                if t == "/": res = l / r
                stack.append(res)
            else:
                # branch 2
                stack.append(t)
        print(stack)

        return int(stack.pop())
