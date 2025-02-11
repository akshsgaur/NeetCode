

'''

Construct Binary Tree from Preorder and Inorder Traversal
Solved 
You are given two integer arrays preorder and inorder.

preorder is the preorder traversal of a binary tree
inorder is the inorder traversal of the same tree
Both arrays are of the same size and consist of unique values.
Rebuild the binary tree from the preorder and inorder traversals and return its root.

Example 1:



Input: preorder = [1,2,3,4], inorder = [2,1,3,4]

Output: [1,2,3,null,null,null,4]
Example 2:

Input: preorder = [1], inorder = [1]

Output: [1]


'''



# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        # Base Case
        if not preorder or not inorder: 
            return None

        #Creating the TreeNode that is the first element of the tree. 
        root = TreeNode(preorder[0])
        #Finding that element in the inorder element, everything before mid will be in the left side
        # of the list. 
        mid = inorder.index(preorder[0])
        # Everything before the mid point will go to the left of the list
        root.left = self.buildTree(preorder[1:mid+1], inorder[:mid])
        # Everything after the mid point will go to the left of the list. 
        root.right = self.buildTree(preorder[mid+1:], inorder[mid+1:])
        return root
        