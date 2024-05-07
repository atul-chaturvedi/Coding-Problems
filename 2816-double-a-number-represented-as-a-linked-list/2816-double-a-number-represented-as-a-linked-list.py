# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverse(self, head):
        prev = None
        current = head
        while(current is not None):
            next = current.next
            current.next = prev
            prev = current
            current = next
        head = prev
        return head
        
    def doubleIt(self, head: Optional[ListNode]) -> Optional[ListNode]:
        head = self.reverse(head)
        temp = head
        carry  =0
        while temp.next != None:
            curr_val = temp.val * 2 + carry
            digit = curr_val %10
            carry = curr_val//10
            temp.val = digit
            temp = temp.next
            
            
        curr_val = temp.val * 2 + carry
        digit = curr_val %10
        carry = curr_val//10
        temp.val = digit
        if carry > 0:
            temp.next = ListNode(carry)
         
        return self.reverse(head)
  
        
                
            
            
        