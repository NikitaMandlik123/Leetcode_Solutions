class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        nums.sort()
        l = 0
        h = len(nums)-1
        
        while(l<h):
            mid = (l+h)//2
            if nums[mid]< mid+1:
                h = mid-1
            else:
                l=mid+1
        return nums[l]
    
    #TC = O(logn)
    #SC = O(1)
    