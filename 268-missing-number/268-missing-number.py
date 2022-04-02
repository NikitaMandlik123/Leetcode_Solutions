class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        s1 = sum(nums)
        s2 = sum(range(0, len(nums)+1))
        return s2-s1
    
    #space complexity: O(1)
    #time complexity: O(n) 