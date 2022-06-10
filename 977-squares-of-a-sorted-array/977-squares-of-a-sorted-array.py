class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        l = 0
        r=len(nums)-1
        ret =[0]*len(nums)
        #for i in nums:
            #ret.append(i ** 2)
        k = len(nums)-1
        while l<=r:
            if abs(nums[l])<abs(nums[r]):
                ret[k] =nums[r] ** 2
                r=r-1
            else:
                ret[k] =nums[l] ** 2
                l= l+1
            k=k-1
        return ret
                
                
                
                
         
                
        
        
            