# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        new_node = head 
        result = new_node
        
        arr =[]
        
        while head!= None:
            arr.append(head.val)
            head = head.next
        
        arr = sorted(arr)
        
        for i in arr:
            new_node.val = i
            new_node = new_node.next
            
        return result