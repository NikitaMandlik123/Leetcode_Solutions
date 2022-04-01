class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        freq = Counter(nums)
        for num, freq in freq.items():
            if freq > 1:
                return True
        return False           
            
            