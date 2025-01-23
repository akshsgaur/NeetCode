
'''

Invert Binary Tree
Solved 
You are given the root of a binary tree root. Invert the binary tree and return its root.

Example 1:



Input: root = [1,2,3,4,5,6,7]

Output: [1,3,2,7,6,5,4]
Example 2:



Input: root = [3,2,1]

Output: [3,1,2]
Example 3:

Input: root = []

Output: []

'''



# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        # Recursive base case, if it reaches the end of the tree, return 
        # None
        if not root: 
            return None 

        #Swapping of the tree
        # Setting tmp to be what is on the left
        tmp = root.left
        # Swapping left to what is on the right
        root.left = root.right
        # setting right to what was previously left
        root.right = tmp
        
        # Calling a recursive function to the left of the current node
        self.invertTree(root.left)
        # Calling a recursive function to the right of the current node
        self.invertTree(root.right)

        #Returning root
        return root
        