class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        output = []
        # Queue in python
        q = collections.deque()
        
        l=r=0
        
        while r<len(nums):
            while q and nums[q[-1]]<nums[r]:
                q.pop()
            q.append(r)
            
            
            if l>q[0]:
                q.popleft()
                
            if (r+1)>=k:
                output.append(nums[q[0]])
                l=l+1
            r = r+1
            
        return output
    
    #TC = O(nlogn)
    #SC = O(n)