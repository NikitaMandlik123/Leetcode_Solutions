class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        count = Counter(nums)
        sol = []
        for i in count:
            if count[i]==1:
                sol.append(i)
        return sol
    
    #TC = O(n)
    #SC = O(n)
        