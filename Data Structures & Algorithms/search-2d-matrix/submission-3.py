class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        n= len(matrix[0])-1
        m=len(matrix)-1
        left = 0
        right = n
        row = 0
        while row <=m:
            if matrix[row][left] <= target <= matrix[row][right]:
                while left <=right: 
                    mid = (right+left)//2
                    if target < matrix[row][mid]:
                        right = mid-1
                    elif target > matrix[row][mid]:
                        left = mid+1
                    elif target == matrix[row][mid]:
                        return True
                    else: 
                        return False 
            else:
                row+=1
        return False 