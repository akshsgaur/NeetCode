from DataStructures.LinkedList import LinkedList

#Given the head of a singly linked list, reverse the list, and return the reversed list.

#Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        #A Prev variable that is initialized to create a None value in the beginning
        prev = None
        # Initialzing cur to be the head
        cur = head
        #Iterating through the linked list
        while cur: 
            #Setting next to be the current's next to keep track of the 
            nxt = cur.next
            # Breaking the tie between cur and cur.next and setting the 
            # next to the prev
            # For example: Before: 0-x->1
            #                       null <- 0 1->2
            cur.next = prev
            # Setting to the prev to the current 
            prev = cur
            # and moving the current to the next
            cur = nxt
        
        #Returning the prev value because that is what will the head in the end
        return prev

    def reverseList_Recursive(self, head):

        if not head:
            return None

        newHead = head

        if head.next:
            print(head.data)
            newHead = self.reverseList_Recursive(head.next)
            head.next.next = head
        head.next = None

        return newHead

llist = LinkedList()
llist.append(1)
# llist.append(2)
# llist.append(3)
# llist.append(4)
# llist.append(5)

solution = Solution()

solution.reverseList_Recursive(llist.head)


