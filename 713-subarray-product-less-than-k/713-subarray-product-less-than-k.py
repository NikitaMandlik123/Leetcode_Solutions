import math
class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        l = 0
        r = 0
        prod = 1
        elements = 0
        while r < len(nums) and l<=r:
            prod = prod*nums[r]
            if prod>=k:
                while prod>=k and l<=r:
                    prod = prod/nums[l]
                    l=l+1
            elements = elements +(r-l) +1
            r = r+1
        return elements