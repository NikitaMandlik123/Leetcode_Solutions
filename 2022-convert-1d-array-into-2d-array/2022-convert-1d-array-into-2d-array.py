class Solution:
    def construct2DArray(self, original: List[int], m: int, n: int) -> List[List[int]]:
        arr2= []
        if m*n!= len(original):
            return []
        
       
        for i in range(0, m*n, n):
            arr2.append(original[i:n+i])
        return arr2
    
    
    #time complexity: O(n^2)
    #space complexity: O(n)
                
            
            
         
            
        