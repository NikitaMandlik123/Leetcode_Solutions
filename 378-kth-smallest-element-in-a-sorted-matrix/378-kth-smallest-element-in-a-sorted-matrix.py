class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        m = len(matrix)
        n = len(matrix[0])
        
        def count(m):
            counter = 0                   
            i = n-1
            j = 0
            
            while i >= 0 and j < n:
                if matrix[i][j] > m:
                    i -= 1
                else:
                    counter += i+1
                    j += 1
            return counter
           
        
        low = matrix[0][0]
        high = matrix[n-1][n-1]
        
        while low <= high:
            m = (low+high)//2
            cnt = count(m)
            if cnt < k:
                low = m + 1
            else:
                cnt1 = count(m-1)
                if cnt1 < k:
                    return m
                high = m-1
        return 0
        
        
        