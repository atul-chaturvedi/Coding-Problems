# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        odd = []
        even = []
        
        dummy1 = head
        dummy2 = head
        
        i  = 1
        while dummy1 != None:
            if i % 2 == 0:
                even.append(dummy1.val)
            else:
                odd.append(dummy1.val)
            
            dummy1 = dummy1.next
            i+=1
            
        i = 0
        j = 0
        while dummy2 != None:
            if i < len(odd):
                dummy2.val = odd[i]
                i+=1
            else:
                dummy2.val = even[j]
                j+=1

            dummy2 = dummy2.next
            
        return head
            
        