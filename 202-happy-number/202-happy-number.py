
class Solution:
    def isHappy(self, n: int) -> bool:
        def Sumofsqr(n):
            sum = 0
            while n!=0:
                if n/10 == 0:
                    sqr = n*n
                    sum = sum+sqr
                    n = int(n/10)
                
                rem = n%10
                sqr = rem*rem 
                sum = sum + sqr
                n = int(n/10)
            return sum
        res = set()
        while n != 1 and n not in res:
            res.add(n)
            n = Sumofsqr(n)
        return n == 1

    
#TC = O(N)
#SC = O(N)
        
    