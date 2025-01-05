'''

Number of Islands
Given a 2D grid grid where '1' represents land and '0' represents water, count and return the number of islands.

An island is formed by connecting adjacent lands horizontally or vertically and is surrounded by water. You may assume water is surrounding the grid (i.e., all the edges are water).

Example 1:

Input: grid = [
    ["0","1","1","1","0"],
    ["0","1","0","1","0"],
    ["1","1","0","0","0"],
    ["0","0","0","0","0"]
  ]
Output: 1

'''

class MySolution:
    def numIslands(self, grid: List[List[str]]) -> int:

        if not grid:
            return 0
        
        rows, cols = len(grid), len(grid[0])
        visit = set()
        islands = 0

        def bfs(r,c):
            q= collections.deque()
            visit.add((r,c))
            q.append((r,c))
            while q: 
                row, col = q.popleft()
                directions = [[1,0],[-1,0],[0,1],[0,-1]]

                for rd, cd in directions: 
                    r,c = row + rd, col+cd
                    if ((r in range(rows) and c in range(cols)) and 
                        (grid[r][c] == "1") and (r,c) not in visit): 
                            q.append((r,c))
                            visit((r,c))


        for r in rows: 
            for c in cols: 
                if grid[r][c] == "1" and (r,c) not in visit:
                    bfs(r,c)
                    islands += 1
            
            
        return islands





class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        # If there is no grid, just return 0
        if not grid: 
            return 0 

        # Get the number of rows and cols
        rows, cols = len(grid), len(grid[0])
        # A set to keep track of visited
        visit = set()
        # The result of number of islands
        islands = 0 


        #The bfs function
        def bfs(r,c):
            # Creating a queue
            q = collections.deque()
            # Adding the row and col to the visited
            visit.add((r,c))
            # Appending it to the queue to iterate and pop from
            q.append((r,c))
            # Traversing through the queue until it is not empty
            while q: 
                # popleft
                row, col = q.popleft()
                #Getting each direction to loop over
                directions = [[1,0],[-1,0],[0,1], [0,-1]]
                # Looping through each direction
                for dr, dc in directions: 
                    # Adding each direction to the row and col
                    r,c = row + dr, col + dc

                    if (
                    # Checking if row and column is in range or not 
                    (r in range(rows) 
                    and c in range(cols))
                    # Checking if the grid value is an island
                    and grid[r][c] == "1"
                    # Checking to see if it in visit or not 
                    and (r,c) not in visit
                    ): 
                        # If it does match this adding it to the queue and iterating through
                        # it in the next loop, also, adding it to visited. 
                        q.append((r,c))
                        visit.add((r,c))

        #Iterate through the number of rows
        for r in range(rows): 
            #Iterate through the number of columns
            for c in range(cols): 
                # If the grid value is equal to one and if the grid value is not
                # in visited, perform breadth first search
                if grid[r][c] == "1" and (r,c) not in visit:
                    # perform bfs on those grid values 
                    bfs(r,c)

                    islands += 1
        
        return islands
        