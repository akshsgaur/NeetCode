'''

Linked List Cycle Detection
Solved 
Given the beginning of a linked list head, return true if there is a cycle in the linked list. Otherwise, return false.

There is a cycle in a linked list if at least one node in the list that can be visited again by following the next pointer.

Internally, index determines the index of the beginning of the cycle, if it exists. The tail node of the list will set it's next pointer to the index-th node. If index = -1, then the tail node points to null and no cycle exists.



'''

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    # Using the tortouise-heir method and if there is a cycle, since the 
    # Gap between the slow and the fast pointer decreases, they 
    # will eventually meet. 
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        #Initiating a slow and a fast pointer
        slow, fast = head, head

        # Going into the loop and checking if fast and fast.next exist or not
        while fast and fast.next: 
            # Moving slow to next
            slow = slow.next
            # Moving fast to next.next
            fast = fast.next.next
            # If they do eventually meeting, They can confidently say that 
            # There is a cycle. 
            if slow == fast:
                # So we return True
                return True
        # This means we hit a null so there is no cycle, so we return false.
        return False
        