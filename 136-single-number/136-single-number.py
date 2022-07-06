class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        Sum = 0
        for i in range(len(nums)):
            Sum = Sum ^ nums[i]
        return Sum
        
        
#TC = O(n)
#SC = O(1)