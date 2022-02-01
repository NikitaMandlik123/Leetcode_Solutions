# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        OrigList = [] 
		
		#Original list
        while head != None:
            if head.val == 0:
                OrigList.append(0)
            else:
                OrigList.append(head.val)
            head = head.next
        
		#new list: reverse the original list
        NewList = OrigList[::-1]
    
        if NewList == OrigList:
            return True
        else:
            return False    
        
            
            