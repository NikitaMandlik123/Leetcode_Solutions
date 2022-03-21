class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        ans = []
        seen = set()
        def dfs(row,col, isUp):
            if row < len(matrix) and row >= 0 and col < len(matrix[0]) and col >= 0 and (row,col) not in seen:
                seen.add((row,col))
                ans.append(matrix[row][col])
                if isUp:
                    dfs(row-1,col,True)
                dfs(row,col+1,False)
                dfs(row+1,col,False)
                dfs(row,col-1,False)
                dfs(row-1,col,True)
        dfs(0,0, False)
        return ans        