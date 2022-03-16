class Solution:
    def construct2DArray(self, original: List[int], m: int, n: int) -> List[List[int]]:
        if m*n != len(original):
            return []
        
        answer = []

        for i in range(0, len(original), n):
            answer.append(original[i:i+n])
            
        return answer        