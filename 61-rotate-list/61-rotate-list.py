# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head:
            return head
        
        length = 1
        tail = head
        #calculate the length and iterate to the tail node
        while tail.next:
            tail = tail.next
            length = length+1
        
        k=k%length
        
        if k==0:
            return head
        #from head, calculate the places until we are rotating the list
        curr = head
        for i in range(length -k -1):
            curr = curr.next
        #save the next to a variable    
        newHead= curr.next
        curr.next= None
        #attach the tail to head
        tail.next = head
        
        #TC = O(n)
        #SC = O(1)
        
        return newHead