class Solution:
    def trap(self, height: List[int]) -> int:
        l = 0
        r = len(height)-1
        area = 0
        l_max = 0
        r_max = 0
        
        while l<r :
            l_max = max(l_max,height[l])
            r_max = max(r_max,height[r])
            
            if height[l]<height[r]:
                area = area + l_max - height[l]
                l=l+1
            else:
                area = area + r_max - height[r]
                r = r-1
        return area