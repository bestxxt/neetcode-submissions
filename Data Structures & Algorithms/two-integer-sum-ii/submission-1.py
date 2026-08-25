class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        length = len(numbers)
        for i1 in range(length):
            for i2 in range(i1 + 1, length):
                if numbers[i1] + numbers[i2] > target:
                    continue
                if numbers[i1] + numbers[i2] == target:
                    return [numbers[i1], numbers[i2]]

