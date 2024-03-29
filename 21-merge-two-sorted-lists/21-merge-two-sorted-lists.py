# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        
        head = Sol = ListNode(0)
        while(list1 and list2):
        # and operation means only true when both lists are not null
            if list1.val<list2.val:
        #if list one has a bigger element then it will get attached to the head of the solution list
                Sol.next = list1
                #iteration
                list1 = list1.next
                Sol = Sol.next
                
            elif (list1.val >= list2.val):
                Sol.next = list2
                list2 = list2.next
                Sol = Sol.next

        Sol.next = list1 or list2
        return head.next
    
    #TC = O(m+n)
    #SC = O(n)
        