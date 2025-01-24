
'''

Merge Two Sorted Linked Lists
Solved 
You are given the heads of two sorted linked lists list1 and list2.

Merge the two lists into one sorted linked list and return the head of the new sorted linked list.

The new list should be made up of nodes from list1 and list2.

Example 1:



Input: list1 = [1,2,4], list2 = [1,3,5]

Output: [1,1,2,3,4,5]
Example 2:

Input: list1 = [], list2 = [1,2]

Output: [1,2]
Example 3:

Input: list1 = [], list2 = []

Output: []


'''





# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        
        # Creating the new head of the linked list that needs to be returned. 
        newhead = ListNode()
        # Setting the tail node that we will keep manipulating according to values encountered. 
        tail = newhead

        #Going through the smallest linked list, whatever it is. So, while they both exist, keep going
        while l1 and l2: 
            # IF the value of l1 is less than l2, then set to tail.next
            # and setting l1 to l1.next 
            if l1.val < l2.val:
                tail.next = l1
                l1 = l1.next
            
            # If the value of l2 is less than l1, then set tail.next to l2
            # and moving l2 to l2.next
            else: 
                tail.next = l2
                l2 = l2.next
            
            #Moving the tail to tail.next to incorporate whatever comes next. 
            tail = tail.next 
        
        # Even if either of the linked list exist after the traversal, then 
        # we set the tail.next to whatever exist. 
        if l1: 
            tail.next = l1
        elif l2: 
            tail.next = l2
        
        #Returning the new head. 
        return newhead.next
