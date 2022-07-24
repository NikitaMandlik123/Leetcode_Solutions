class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        #Sort according to th e first element
        intervals.sort(key =lambda x: x[0])
        #result
        res =[]
        for i in intervals:
			
            if not res or res[-1][-1] < i[0]:
                res.append(i)
			# otherwise, there is overlap,
			#so we merge the current and previous intervals.
            else:
                res[-1][-1] = max(res[-1][-1], i[-1])
        return res
    
    
    #tc = O(nlogn)
    #sc = O(n)