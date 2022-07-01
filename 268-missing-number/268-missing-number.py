class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        missing=0
        for i in nums:
            missing=missing^i
        for i in range(len(nums)):
            missing=missing^i
        missing=missing^(i+1)
        return missing
    
    #TC = O(N)
    #SC = O(1)
    
        