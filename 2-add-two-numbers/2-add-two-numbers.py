# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = new = ListNode(0)
        car = 0
        while l1 or l2 or car:
            if l1:
                car += l1.val
                l1 = l1.next
            if l2:
                car += l2.val
                l2 = l2.next
            new.next = ListNode(car%10)
            new = new.next
            car //= 10
        return dummy.next
    
#TC = O(n+m)
#SC = O(n)
            