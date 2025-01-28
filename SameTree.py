

'''

Same Binary Tree
Solved 
Given the roots of two binary trees p and q, return true if the trees are equivalent, otherwise return false.

Two binary trees are considered equivalent if they share the exact same structure and the nodes have the same values.

Example 1:



Input: p = [1,2,3], q = [1,2,3]

Output: true
Example 2:



Input: p = [4,7], q = [4,null,7]

Output: false
Example 3:



Input: p = [1,2,3], q = [1,3,2]

Output: false

'''



# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:

    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        # If both the left and the right side are empty, return true
        if not p and not q: 
            return True 
        
        # If one of them is empty and the other one is not, you have to return False
        if not p or not q:
            return False
        
        # If the values of the node are not equal, you again, return False
        if p.val != q.val:
            return False
        
        # The recursive call, we will then traverse through the left and the right side to check if the conditions above have been met, 
        # If the conditions have been met in all the recursive functions, we can then confidently return True. 
        return(self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right))
        