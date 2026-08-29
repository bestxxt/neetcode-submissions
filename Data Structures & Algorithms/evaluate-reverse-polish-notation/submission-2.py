class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for t in tokens:
                # branch 1
                if t == "+": 
                    r = int(stack.pop())
                    l = int(stack.pop())
                    res = l + r
                    stack.append(res)
                elif t == "-": 
                    r = int(stack.pop())
                    l = int(stack.pop())
                    res = l - r
                    stack.append(res)
                elif t == "*": 
                    r = int(stack.pop())
                    l = int(stack.pop())
                    res = l * r
                    stack.append(res)
                elif t == "/": 
                    r = int(stack.pop())
                    l = int(stack.pop())
                    res = l / r
                    stack.append(res)
                else:
                    # branch 2
                    stack.append(t)
        print(stack)

        return int(stack.pop())
