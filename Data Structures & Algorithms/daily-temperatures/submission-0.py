class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        temp = [] # highest temp -> lower temp
        res = [0] * len(temperatures)
        for t in range(len(temperatures)):
            while len(temp) != 0 and temperatures[t] > temperatures[temp[-1]]:
                # loop to find every item
                target = temp.pop()
                res[target] = t - target
            temp.append(t)
        return res
