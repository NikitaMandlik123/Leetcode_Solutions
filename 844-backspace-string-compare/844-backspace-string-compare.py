class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        new1 = []
        new2= []
        
        for ele in s:
            if ele!="#":
                new1.append(ele)
            elif new1:
                new1.pop()
        for elem in t:
            if elem!="#":
                new2.append(elem)
            elif new2:
                new2.pop()
                
        if new1==new2:
            return True
        else:
            return False
        