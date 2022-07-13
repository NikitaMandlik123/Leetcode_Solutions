class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        low_bits = high_bits = 0
        for num in nums:
            low_bits = ~high_bits & (low_bits ^ num)
            high_bits = ~low_bits & (high_bits ^ num)
        return low_bits
    
    #TC = O(n)
    #SC = O(1)