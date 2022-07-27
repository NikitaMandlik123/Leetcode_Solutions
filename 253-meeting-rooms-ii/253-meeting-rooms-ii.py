class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        start = sorted([i[0] for i in intervals])
        end = sorted([i[1] for i in intervals])
        
        sol=0
        count = 0
        s = 0
        e = 0
        
        while s <len(intervals):
            if start[s]<end[e]:
                count=count+1
                s=s+1
            else:
                e=e+1
                count=count-1
            sol=max(sol,count)
        return sol