class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m,n = len(matrix), len(matrix[0])
        top, bot = 0, m-1
        while top<=bot:
            mid = (top+bot)//2
            if matrix[mid][0] > target:
                bot = mid-1
            elif matrix[mid][-1] < target:
                top = mid+1
            else:
                break
        if not (top<=bot):
            return False
        mid=(top+bot)//2
        left, right = 0, n-1
        while left<=right:
            mid_mid = (left+right)//2
            if matrix[mid][mid_mid] < target:
                left = mid_mid +1
            elif matrix[mid][mid_mid] > target:
                right = mid_mid -1
            else:
                return True
        return False