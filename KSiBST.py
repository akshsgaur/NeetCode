


"""


Kth Smallest Integer in BST
Solved 
Given the root of a binary search tree, and an integer k, return the kth smallest value (1-indexed) in the tree.

A binary search tree satisfies the following constraints:

The left subtree of every node contains only nodes with keys less than the node's key.
The right subtree of every node contains only nodes with keys greater than the node's key.
Both the left and right subtrees are also binary search trees.
Example 1:



Input: root = [2,1,3], k = 1

Output: 1
Example 2:



Input: root = [4,3,5,2,null], k = 4

Output: 5


"""




# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        # Keeping a stack to keep track of all the elements 
        # that we add and remove from the tree
        stack = []
        # Initializing the current node that we will manipulate as we
        # traverse through the tree
        cur = root
        # We need to see if the stack or the current node is empty, but mostly 
        # it's the stack that we need to be mindful off, that is our base case
        while stack or cur: 
            
            # Traversing through the left part of the code to find the smallest value
            while cur: 
                # Appending it to the stack
                stack.append(cur)
                # Moving to the left of the list
                cur = cur.left

            # Once we reach the leftmost element, we pop it from the stack. 
            cur = stack.pop()
            # Decrementing k value
            k -= 1
            # We check if k is 0 or not. 
            if k == 0:
                # We can confidently return the value
                return cur.val

            # For the situation where k is not 0, we traverse through the right side of the 
            # list. 
            cur = cur.right 