class Solution:
    def maxArea(self, height: List[int]) -> int:
        left = 0
        right = len(height)-1
        result = 0
        while left < right:
            solution = (right - left) * min(height[left], height[right])
            result = max(solution,result)
            if height[left]<height[right]:
                left = left+1
            else:
                right = right-1
        return result      
        