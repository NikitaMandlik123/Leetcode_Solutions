class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m = len(matrix)
        n = len(matrix[0])
        r =0
        c = n-1
        while r!=m and c>=0:
            if target == matrix[r][c]:
                return True
            elif target>matrix[r][c]:
                r=r+1
            else:
                c=c-1
        return False
            
        
#TC = O(logn*m)
#SC = O(1)