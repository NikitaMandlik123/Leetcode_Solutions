# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        slow = head
        fast = head
        while fast.next!=None and fast.next.next!=None:
            slow = slow.next
            fast = fast.next.next
        if fast.next==None:
            return slow
        return slow.next
            
#TC = O(N)
#SC = O(1)