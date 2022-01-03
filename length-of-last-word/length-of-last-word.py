class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        length=0
        a= s.strip()
        
        for i in range(len(a)):
            if a[i] == " ":
                 length=0
            else:
                 length=length+1
        return length