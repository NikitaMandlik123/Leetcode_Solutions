class Solution:
    def bitwiseComplement(self, n: int) -> int:
        if n == 0:
            return 1
        else:
            result = 0
            factor = 1
            
            while(n > 0):
                if n%2 ==0:
                    result = result+ factor * 1 
                else:
                    result = result+ factor * 0
                factor *= 2
                n //= 2
            return result
        
    #TC = O(n)
    #SC = O(1)