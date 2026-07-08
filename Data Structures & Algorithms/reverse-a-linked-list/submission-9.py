# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        """
        Reverses Linked List
        >> reverseList(head  = [0,1,2,3])
        [3,2,1,0]
        """
        # A linked list is an object that stores a val and the next ListNode
        # ListNode being the object 
        # The core idea: we want to reverse the links between each listnode
        # by adjusting what the next listnode is going to be
        # since we want to change it in place, we cannot create a new linkedlist
        # therefore --> two pointers
        right_pointer = None
        left_pointer = head
        # we go through the linked list until left_pointer points at nothing 
        # --> None
        while left_pointer: 
            next = left_pointer.next
            left_pointer.next = right_pointer
            right_pointer = left_pointer
            left_pointer = next
        return right_pointer

    
