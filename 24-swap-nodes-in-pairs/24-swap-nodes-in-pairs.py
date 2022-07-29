# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0,head)
        prev =dummy
        curr= head
        
        while curr and curr.next:
            #set the next pair with a pointer
            nxtPair = curr.next.next
            second = curr.next
            #swappind the nextr nodes
            second.next = curr
            curr.next = nxtPair
            prev.next = second
            #update the pointers
            prev = curr
            curr=nxtPair
        return dummy.next
    
    
#TC = O(n)
#SC = O(n)
    
        