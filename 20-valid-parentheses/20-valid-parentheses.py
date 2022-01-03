class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for i in s:
            if i == "(" or i == "{" or i == "[":
                stack.append(i) 
            #empty stack    
            elif len(stack) <= 0:
                return False
            #if ) is in the s and ( does not exists in the stack.pop()
            elif i == ")" and stack.pop() != "(":
                return False
            elif i == "]" and stack.pop() != "[":
                return False
            elif i == "}" and stack.pop() != "{":
                return False
        if len(stack) == 0:
            return True
        return False
 
