# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy1 = head
        dummy2 = head
        values =  []
        
        while dummy1 != None:
            values.append(dummy1.val)
            dummy1 = dummy1.next
            
        
        values.sort()
        
        i=0
        while dummy2 != None:
            dummy2.val = values[i]
            dummy2 = dummy2.next
            i+=1
            
        
        return head
            
        