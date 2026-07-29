class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        ## search through each row of matrix one by one,
        ## if we find the target in this row return true
        ## else move to the next row and search through it
        for row in matrix:
            if self.bs(row, target):
                return True
            else:
                continue
        
        return False
    
    
    def bs(self, row: List[int], target: int) -> bool:
        left, right = 0, len(row) - 1

        while left <= right:
            
            mid = (right + left) // 2

            if row[mid] == target:
                return True
            elif row[mid] < target:
                left = mid + 1
            else:
                right = mid - 1

        return False
        
        