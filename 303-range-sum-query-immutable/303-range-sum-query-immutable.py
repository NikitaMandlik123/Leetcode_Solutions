class NumArray:

    def __init__(self, nums: List[int]):
        for i in range(1, len(nums)):
            nums[i] += nums[i-1]
        self.prefix = nums        
        

    def sumRange(self, left: int, right: int) -> int:
        ans = self.prefix[right]
        if left: ans -= self.prefix[left-1]
        return ans         
        


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)