class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        
        sol = set([])
        p = sorted([n for n in nums if n>0])
        p_set = set(p)
        z = [n for n in nums if n == 0]
        neg = sorted([n for n in nums if n<0])
        neg_set = set(neg)
        
        
        
   
        if len(z)>=3:
            sol.add((0,0,0))
            
            
    
        if len(z)>0:
            for n in neg:
                if -n in p_set:
                    sol.add((n,0,-n))
                    
                    
                    
     
        n = len(neg)
        for i in range(n):
            for j in range(i+1,n):
                diff = -(neg[i]+neg[j])
                if diff in p_set:
                    sol.add((neg[i],neg[j],diff))
                    
                    
        
        n = len(p)
        for i in range(n):
            for j in range(i+1,n):
                diff = -(p[i]+p[j])
                if diff in neg_set:
                    sol.add((diff,p[i],p[j]))
        return list(sol)        