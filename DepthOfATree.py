'''
Maximum Depth of Binary Tree
Solved 
Given the root of a binary tree, return its depth.

The depth of a binary tree is defined as the number of nodes along the longest path from the root node down to the farthest leaf node.

Example 1:



Input: root = [1,2,3,null,null,4]

Output: 3
Example 2:

Input: root = []

Output: 0
Constraints:

0 <= The number of nodes in the tree <= 100.
-100 <= Node.val <= 100

'''


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepthRecursive(self, root: Optional[TreeNode]) -> int:
        #Recursive base case
        if not root: 
            #return 0
            return 0
        # Creating the recursive stack in which we will decide which which one has the 
        # maximum depth. 
        return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))

    def maxDepth(self, root): 

        # A queue to keep track of all the elements that are encountered
        q = deque()
        # If there is a root, then we append that to the queue, if not, there
        # is nothing in the queue to append and we will return level = 0, making 
        # this is the edge case whereby there is no root to begin with. 
        if root: 
            q.append(root)

        #Initiating the res level
        level = 0
        # Going through the q until it is empty. 
        while q: 

            #Seeing all the children of the root that is being evaluated. 
            for i in range(len(q)):
                # Popping the left most element, that will give us the current 
                # node. 
                subroot = q.popleft()
                # If there is a left to that node, we append it to the 
                # queue
                if subroot.left:
                    q.append(subroot.left)
                
                #If there is a right to that node, we append that to the queue 
                # as well. 
                if subroot.right:
                    q.append(subroot.right)
            # Once we have iterated through node and it's children, we 
            # confidently increment the level by 1. 
            level += 1
        
        #Return the level. 
        return level