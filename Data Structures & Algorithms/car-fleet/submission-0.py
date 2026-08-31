class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        # sort
            pairs = list(zip(position, speed))
            pairs.sort(key=lambda x: x[0], reverse=True)
            position, speed = zip(*pairs)
            time = []
            for car in pairs:
                time.append((target - car[0]) / car[1])

            stack = []
            # print(position)
            # print(time)
            stack.append(time[0])
            for i in range(1, len(position)):
                if time[i] > stack[-1]:
                    stack.append(time[i])
                

            return len(stack)
