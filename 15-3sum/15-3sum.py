class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        ret = set()
        for i in range(len(nums)-1):
            n3 = -nums[i]
            l = i+1
            r = len(nums)-1
            
            while l<r:
                if nums[l]+nums[r]<n3:
                    l=l+1
                elif nums[l]+nums[r]>n3:
                    r =r-1
                else:
                    ret.add((nums[i],nums[l],nums[r]))
                    l=l+1
                    r = r-1
        return ret
                
#time comp = O(n^2)
#space comp = O(n)