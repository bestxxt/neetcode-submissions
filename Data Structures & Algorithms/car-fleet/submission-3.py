class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        pairs = sorted(zip(position, speed), reverse=True)  # 按位置从大到小排序
        stack = []
        for pos, spd in pairs:
            t = (target - pos) / spd
            if not stack or t > stack[-1]:
                stack.append(t)
            # 如果 t <= stack[-1]，说明追上了前车，合并，不入栈
        return len(stack)