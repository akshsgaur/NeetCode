
'''

Reorder Linked List
Solved 
You are given the head of a singly linked-list.

The positions of a linked list of length = 7 for example, can intially be represented as:

[0, 1, 2, 3, 4, 5, 6]

Reorder the nodes of the linked list to be in the following order:

[0, 6, 1, 5, 2, 4, 3]

Notice that in the general case for a list of length = n the nodes are reordered to be in the following order:

[0, n-1, 1, n-2, 2, n-3, ...]

You may not modify the values in the list's nodes, but instead you must reorder the nodes themselves.

'''



class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        #setting slow and fast pointer to track the middle of the list
        slow, fast = head, head.next

        #Iterating to reach the middle of the list
        while fast and fast.next: 
            slow = slow.next
            fast = fast.next.next
        
        #Setting second to slow.next
        second = slow.next 
        # changing the pointers
        prev = slow.next = None

        #Reversing the list
        while second: 
            tmp = second.next 
            second.next = prev
            prev = second
            second = tmp
        

        first, second = head, prev
        #Reordering the list
        while second: 
            tmp1, tmp2 = first.next, second.next
            first.next = second
            second.next = tmp1
            first, second = tmp1, tmp2