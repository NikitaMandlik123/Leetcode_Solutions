class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        countred = 0
        countwh = 0
        countbl = 0
        for a in nums:
            if a == 0:
                countred = countred + 1
            elif a == 1:
                countwh = countwh + 1
            else:
                countbl = countbl +1
                
        for i in range(countred):
            nums[i] = 0
        for j in range(countred,countred+countwh,1):
            nums[j]= 1
        for k in range(countred+countwh,countred+countwh+countbl,1):
            nums[k] = 2
            
            
                