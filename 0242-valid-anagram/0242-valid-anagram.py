class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        if len(s)!= len(t):
            return False
        
        if sorted(s)==sorted(t):
             return True
        else:
             return False
        
         
#         s1 = list(s)
#         t1 = list(t)
        
#         if len(s1)!=len(t1):
#             return False
#         if sorted(s1)==sorted(t1):
#             return True
#         else:
#             return False

         