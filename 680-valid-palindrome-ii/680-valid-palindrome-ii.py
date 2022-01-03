class Solution:
    def validPalindrome(self, s: str) -> bool:
        l=0
        r=len(s)-1
        
        def check_palindrome(s):
            return s == s[::-1]
        while l < r:
            if s[l] != s[r]:
                return check_palindrome(s[l:r]) or check_palindrome(s[l+1:r+1])
            l +=1
            r -=1
        return True