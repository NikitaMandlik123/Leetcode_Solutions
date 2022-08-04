class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        l=0
        total = 0
        res = float("inf")
        
        for r in range(len(nums)):
            total = total + nums[r]
            while total>=target:
                res = min(r-l+1,res)
                total = total -nums[l]
                l= l+1
        return 0 if res==float("inf") else res
    
    
    #TC = O(nlogn)
    #SC = O(1)