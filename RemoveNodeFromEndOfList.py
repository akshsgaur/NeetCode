

'''
Remove Node From End of Linked List
Solved 
You are given the beginning of a linked list head, and an integer n.

Remove the nth node from the end of the list and return the beginning of the list.

Example 1:

Input: head = [1,2,3,4], n = 2

Output: [1,2,4]
Example 2:

Input: head = [5], n = 1

Output: []

'''



# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:

        #Creating a dummy node to keep track of the prev node to replace
        dummy = ListNode(0, head)
        #Initializing left to be the dummy
        left = dummy 
        # setting right to be the head
        right = head 

        #Shifting right by n values to give that headway
        while n > 0: 
            right = right.next
            n -= 1
        
        # Traversing through the linked list until right reaches the end of the list
        while right:
            left = left.next 
            right = right.next 
        
        # Deleting the node we want to delete
        left.next = left.next.next
        #returning the head of the list. 
        return dummy.next