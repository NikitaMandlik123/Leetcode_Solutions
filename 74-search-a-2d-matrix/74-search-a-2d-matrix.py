class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        col = len(matrix[0])
        l = 0
        h = (len(matrix)*col)-1
        
        while(l<=h):
            mid = (l+h)//2
            r = mid//col
            c = mid%col
            if matrix[r][c]==target:
                return True
            elif matrix[r][c]>target:
                h = mid-1
            else:
                l = mid+1
        return False