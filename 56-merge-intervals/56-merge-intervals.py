class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda x: x[0])

        solution = []
        for interval in intervals:
            # if the list of merged intervals is empty or if the current
            # interval does not overlap with the previous, simply append it.
            if not solution or solution[-1][1] < interval[0]:
                solution.append(interval)
            else:
            # otherwise, there is overlap, so we merge the current and previous
            # intervals.
                solution[-1][1] = max(solution[-1][1], interval[1])

        return solution
    
    
    #TC = O(nlogn)
    #SC = O(1)