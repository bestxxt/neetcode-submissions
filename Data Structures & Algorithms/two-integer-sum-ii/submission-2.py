class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        res = {}
        for i in range(len(numbers)):
            res[numbers[i]] = target - numbers[i]

        for key, value in res.items():
            if value in res:
                return(sorted([key,value]))
        