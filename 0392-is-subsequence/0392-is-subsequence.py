class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        i=0
        j=0
        
        s1 = list(s)
        t1 = list(t)
        
        while(j<len(s1) and i<len(t1)):
            if s1[j]==t1[i]:
                j+=1
                i+=1
            else:
                i+=1
            
               
        if j == len(s1):
            return True
        else:
            return False
            