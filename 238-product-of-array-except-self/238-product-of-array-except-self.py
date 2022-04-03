class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n= len(nums)
        ans = [1] * n
        
        for i in range(n):
            if i != 0:
                ans[i] = ans[i-1] * nums[i-1]
                
        p = nums[n-1]
        
        
        for i in range(n-1, 0, -1):
            ans[i-1] = ans[i-1] * p
            p= p*nums[i-1]
            
        return ans    

            
            
            
           