# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        Olist= []
        
        while head!=None:
            if head.val==0:
                Olist.append(0)
            else:
                Olist.append(head.val)
            head=head.next
        Nlist = Olist[::-1]
        if Olist==Nlist:
            return True
        else:
            return False
        
        
#TC = O(n)
#SC = O(n)