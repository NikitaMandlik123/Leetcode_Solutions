class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        l =0
        h = len(nums)-1
        while(l<=h):
            mid = (l+h)//2
            if nums[mid]==target or target == nums[l] or target == nums[h]:
                return True
            elif nums[mid]==nums[l] or nums[mid]==nums[h]:
                h-=1
                l+=1
            elif nums[l]<=nums[mid]:
                if target > nums[mid] or target < nums[l]:
                     l = mid + 1
                else:
                    h = mid -1
            
            else:
                if target < nums[mid] or target > nums[h]:
                    h = mid -1 
                else:
                     l = mid+1
            
        return False