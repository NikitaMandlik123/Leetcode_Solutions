class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        n = len(s)
        ans = 0
        l = 0
        mp={}
        
        for r in range(n):
            if s[r] in mp:
                l = max(mp[s[r]],l)
            ans = max(ans, r-l+1)
            mp[s[r]] = r+1
        return ans
        
        
    #TC =O(n)
    #SC = O(n)