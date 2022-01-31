# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
	    newList = []
	    while head:
		    newList.append(head)
		    head = head.next
	    return newList[len(newList)//2]        
        