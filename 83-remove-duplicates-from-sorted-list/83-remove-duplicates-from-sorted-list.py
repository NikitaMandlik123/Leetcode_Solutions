# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:

        Olist = head
        while Olist:
            while Olist.next and Olist.next.val==Olist.val:
                Olist.next = Olist.next.next
            Olist = Olist.next
        return head