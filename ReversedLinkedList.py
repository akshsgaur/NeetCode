from DataStructures.LinkedList import LinkedList

#Given the head of a singly linked list, reverse the list, and return the reversed list.

#Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


class Solution:
    def reverseListIterative(self, head):

        if head == None:
            return
        if head.next == None:
            return head

        prev, curr = None, head
        while curr:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt
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


