class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        l=0
        h=len(letters)-1
        sol=letters[0]
        while(l<=h):
            mid=(l+h)//2
            if letters[mid]>target:
                h=mid-1
                sol=letters[mid]
            else:
                l=mid+1
        return sol
        
        
        #TC = O(nlogn)
        