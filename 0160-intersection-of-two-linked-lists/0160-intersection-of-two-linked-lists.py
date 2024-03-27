# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        # Function to calculate the length of a linked list
        def get_length(node):
            length = 0
            while node:
                length += 1
                node = node.next
            return length
        
        # Get the lengths of both linked lists
        lenA = get_length(headA)
        lenB = get_length(headB)
        
        # Move the pointer of the longer linked list to make it equal in length to the shorter one
        while lenA > lenB:
            headA = headA.next
            lenA -= 1
        
        while lenB > lenA:
            headB = headB.next
            lenB -= 1
        
        # Traverse both linked lists until intersection or end
        while headA and headB:
            if headA == headB:
                return headA
            headA = headA.next
            headB = headB.next

        
        # No intersection found
        return None
            