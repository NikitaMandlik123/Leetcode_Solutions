class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        ret = set()
        if len(nums) < 4:
            return []
        for i in range(len(nums)-2):
            for j in range(i+1,len(nums)-2,1):
                l= j+1
                r = len(nums)-1
                while l<r:
                    if nums[l]+nums[r]+ nums[i]+nums[j] <target:
                        l=l+1
                    elif nums[l]+nums[r]+ nums[i]+nums[j] >target:
                        r = r-1
                    else:
                        #ret.add((nums[i],nums[j],nums[l],nums[r]))
                        if (nums[i],nums[j],nums[l],nums[r]) not in ret:
                            ret.add((nums[i],nums[j],nums[l],nums[r]))
                        l=l+1
                        r = r-1
         
        return ret
    