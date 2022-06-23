# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        if not head :
            return head
        n = head
        while n!= None and n.next!= None:
            if n.next.val == val:
                n.next = n.next.next
            else:
                n = n.next
            
        if head.val == val:
            head = head.next
        
        return head
    
#TC = O(n)
#SC = O(1)