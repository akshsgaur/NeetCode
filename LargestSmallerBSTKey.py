'''

Largest Smaller BST Key
Given a root of a Binary Search Tree (BST) and a number num, implement an efficient function findLargestSmallerKey that finds the largest key in the tree that is smaller than num. If such a number doesn't exist, return -1. Assume that all keys in the tree are nonnegative.

Analyze the time and space complexities of your solution.

For example:

For num = 17 and the binary search tree below:

Binary tree

Your function would return:

14 since it`s the largest key in the tree that is still smaller than 17.

Constraints:

[time limit] 5000ms
[input] Node rootNode
[output] integer



'''

# A node 
class Node:
    # Constructor to create a new node
    def __init__(self, key: int):
        self.key: int = key
        self.left: Optional['Node'] = None
        self.right: Optional['Node'] = None
        self.parent: Optional['Node'] = None

# A binary search tree 
class BinarySearchTree:
    # Constructor to create a new BST
    def __init__(self):
        self.root: Optional[Node] = None

    def find_largest_smaller_key(self, num: int) -> Optional[int]:
        #Setting the Largest number to -1 just in case we dont find a number smaller than the num value. 
        LargestNumber = -1
        #Setting the dfs function which takes a node and a LargestNumber
        def dfs(node, LargestNumber): 
            #Base case if it does not find a node, then just return the Largest Number
            if not node: 
                return LargestNumber
            
            # If node.key is greater than the num, then traverse through the left of the tree. 
            # There is no need to update the Largest number because we are looking for a number that is less than num. 
            if node.key >= num:
                return dfs(node.left, LargestNumber)

            # If node.key < num, update the Largest Number accordingly, if they key is create than current Largest Number, than 
            # update the LargestNumber and then traverse through the right of the node. 
            else: 
                LargestNumber = max(node.key, LargestNumber)
                return dfs(node.right, LargestNumber)
           
        
        return dfs(self.root, LargestNumber)
