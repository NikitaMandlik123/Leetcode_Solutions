class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        low = high = 0
        for i in nums:
            low = ~high & (low ^ i)
            high = ~low & (high ^ i)
        return low
    
    #TC = O(n)
    #SC = O(1)