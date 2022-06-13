class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        ret = 0
        dif = float('inf')
        for i in range(len(nums)-1):
            l = i+1
            r = len(nums)-1
            
            while l<r:
                res = nums[l]+nums[r]+nums[i]
                if res==target:
                    return res
                if abs(res -target) <=dif:
                    dif = abs(res-target)
                    ret = res
                if res <target:
                    l = l+1
                else:
                    r = r-1
                    
        return ret