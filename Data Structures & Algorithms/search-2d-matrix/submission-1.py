class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # edge case
        if target > matrix[-1][-1] or target < matrix[0][0]:
            return False
        #-----------
        # get row
        lo = 0 
        hi = len(matrix) - 1
        row = 0
        while lo <= hi:
            mid = (lo + hi) // 2
            if matrix[mid][0] == target:
                return True
            if target > matrix[mid][0]:
                lo = mid + 1
            elif target < matrix[mid][0]:
                hi = mid - 1
        row = hi    
        # we have row here
        # print("row:", row)
        lo = 0 
        hi = len(matrix[0]) - 1
        while lo <= hi:
            mid = (lo + hi) // 2
            if matrix[row][mid] == target:
                return True
            if target > matrix[row][mid]:
                lo = mid + 1
            elif target < matrix[row][mid]:
                hi = mid - 1
        return False