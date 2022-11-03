class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        
        
        temp = s.strip()
        q = temp.split(' ')
        n = len(q)-1  
        #return q
        return len(q[n])