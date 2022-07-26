class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key = lambda x :x[1])
    
    
        count = 0
        i = 1
        while i < len(intervals):
            if intervals[i][0] < intervals[i-1][1]:
            
                
                intervals.pop(i)
                count+=1
        
            else:
                i+=1
        
            
        return count
    
    #TC = O(nlogn)
    #SC = O(1)