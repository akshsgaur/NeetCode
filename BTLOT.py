


"""

Binary Tree Level Order Traversal
Solved 
Given a binary tree root, return the level order traversal of it as a nested list, where each sublist contains the values of nodes at a particular level in the tree, from left to right.

Example 1:



Input: root = [1,2,3,4,5,6,7]

Output: [[1],[2,3],[4,5,6,7]]
Example 2:

Input: root = [1]

Output: [[1]]
Example 3:

Input: root = []

Output: []



"""



# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        # Initializing the result list
        res = []

        #Following the BFS functionality, we are initializing the queue
        q = collections.deque() 
        #Appending root node to the queue to traverse
        q.append(root)

        #While the queue is empty 
        while q: 
            # Length of the queue at that level
            qLen = len(q)
            # Initializing list that needs to be appended at that time. 
            level = []
            # Traversing through each element at that level
            for i in range(qLen):
                # Popping each node to analyze
                node = q.popleft()
                # Updating the queue to incorporate the children of the node
                # We have to check if the node exists or not. 
                if node: 
                    level.append(node.val)
                    q.append(node.left)
                    q.append(node.right)
                    
            # If there is a level, we append it to the result list. 
            if level:
                res.append(level)

        #Returning the list. 
        return res