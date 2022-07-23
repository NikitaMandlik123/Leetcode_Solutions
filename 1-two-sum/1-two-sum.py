class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        l = 0
        r = len(nums) - 1
        while l <= r:
            if nums[l] + nums[r] == target:
                return [l, r]
            r -= 1
            if r == l:
                l += 1
                r = len(nums)-1  
                    
                    
                    
#TC = O(n)
#SC = O(1)