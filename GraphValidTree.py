'''
Graph Valid Tree
Given n nodes labeled from 0 to n - 1 and a list of undirected edges (each edge is a pair of nodes), write a function to check whether these edges make up a valid tree.

Example 1:

Input:
n = 5
edges = [[0, 1], [0, 2], [0, 3], [1, 4]]

Output:
true
Example 2:

Input:
n = 5
edges = [[0, 1], [1, 2], [2, 3], [1, 3], [1, 4]]

Output:
false

'''

class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if not n:
            return True
        
        adj = {i:[] for i in range(n)}
        for n1, n2 in edges: 
            adj[n1].append(n2)
            adj[n2].append(n1)

        visit = set()
        def dfs(i, prev):
            if i in visit:
                return False
            
            visit.add(i)
            for j in adj[i]:
                if j == prev:
                    continue
                if not dfs(j,i):
                    return False
            return True
        
        return True and n == len(visit)

        
class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        # if the graph is empty, return True 
        if not n:
            return True
        
        #Creating the adjacency list initially with a empty list
        adj = {i:[] for i in range(n)}
        # create the undirected graph
        for n1, n2 in edges: 
            adj[n1].append(n2)
            adj[n2].append(n1)
        
        #Creating a visit set to check for loops
        visit = set()
        #Creating a DFS function to traverse through the tree
        def dfs(i, prev):
            # If i is in visit, there is a loop and we need to return False
            if i in visit:
                return False
            #Add i to the visit list
            visit.add(i)
            # Traverse through neighbors of i
            for j in adj[i]: 
                # j == prev value, that means we are traversing through 
                # a visited parent of the node, so we continue
                if j == prev:
                    continue
                
                # Recursive function and if it returns false, return false
                if not dfs(j, i):
                    return False
            return True
        
        return dfs(0,-1) and n == len(visit)