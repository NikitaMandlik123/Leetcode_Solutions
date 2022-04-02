class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        nums2 = list(range(1,len(nums)+1))
        a = set(nums2) - set(nums)
        return a
       
        # time complexity : O(n)
        #space complexity : O(1)