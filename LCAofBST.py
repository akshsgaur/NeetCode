

'''

Lowest Common Ancestor in Binary Search Tree
Solved 
Given a binary search tree (BST) where all node values are unique, and two nodes from the tree p and q, return the lowest common ancestor (LCA) of the two nodes.

The lowest common ancestor between two nodes p and q is the lowest node in a tree T such that both p and q as descendants. The ancestor is allowed to be a descendant of itself.

Example 1:



Input: root = [5,3,8,1,4,7,9,null,2], p = 3, q = 8

Output: 5
Example 2:



Input: root = [5,3,8,1,4,7,9,null,2], p = 3, q = 4

Output: 3
Explanation: The LCA of nodes 3 and 4 is 3, since a node can be a descendant of itself.

Constraints:

2 <= The number of nodes in the tree <= 100.
-100 <= Node.val <= 100
p != q
p and q will both exist in the BST.

'''



# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        # Setting the cur value to the root to traverse
        cur = root

        # This is to iterate through the tree
        while cur: 
            # If both the values of p and q are greater than the current node
            # it is safe to say that the LCA would be in the right subtree, so 
            # we traverse through the right side of the tree
            if p.val > cur.val and q.val > cur.val:
                cur = cur.right
            
            # If both the values of p and q are less than the current node
            # it is safe to say that the LCA would be in the left subtree, so 
            # we traverse through the right side of the tree
            elif p.val < cur.val and q.val < cur.val:
                cur = cur.left
            
            # This would mean that either the p or q is equal to the node, 
            # or there is a split in the tree, either way, there is a 
            # that would make it the LCA 
            else: 
                return cur
