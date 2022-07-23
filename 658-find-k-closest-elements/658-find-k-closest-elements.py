class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        l = 0
        h = len(arr)-k #as we need a window
        
        while l<h:
            mid = (l+h)//2
            #right element is closer
            if x-arr[mid]>arr[mid+k]-x:
                l=mid+1
            else:
                h=mid
        return arr[l:l+k]
                
        
        
#TC = O(logn + k)
#SC = O(1)