# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        
    
        newList = ListNode(0)
        newList.next = head
    
        prev = newList
        curr = newList.next
    
        # find the position left (starting of the slice)
        for i in range(1,left):
            curr = curr.next
            prev = prev.next
    
    
        # reverse the part left to right
        for i in range(right-left):
            temp = curr.next
            curr.next = temp.next
            temp.next  = prev.next
            prev.next = temp
    
        return newList.next
    
    #TC  = O(right)
    #SC = O(right)