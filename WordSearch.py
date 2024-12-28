'''

Word Search
Given a 2-D grid of characters board and a string word, return true if the word is present in the grid, otherwise return false.

For the word to be present it must be possible to form it with a path in the board with horizontally or vertically neighboring cells. The same cell may not be used more than once in a word.

Example 1:
Input: 
board = [
  ["A","B","C","D"],
  ["S","A","A","T"],
  ["A","C","A","E"]
],
word = "CAT"

Output: true


Time complexity: O(n * m * 4^m) <- m is the word
https://neetcode.io/problems/search-for-word
'''


class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:

        ROWS, COLS = len(board), len(board[0])
        path = set()

        def dfs(r, c, i): 

            if i == len(word): 
                return True
            
            if (#r and c have to be positive
                r<0 or c<0 or 
                # r and c should be in bounds
                r >= ROWS or c >= COLS or
                #If the word in the current position does not equal the board
                word[i] != board[r][c] or
                #If the word has been visited before
                (r,c) in path
            ):
                return False

            #Because it does not meet the criteria above, it is safe to explore the word further.
            path.add((r,c))
            res = ( dfs(r+1, c, i+1) or
                    dfs(r-1, c, i+1) or
                    dfs(r, c+1, i+1) or
                    dfs(r, c-1, i+1)

            )
            path.remove((r,c))
            return res
        
        #Check for each row and column that word exists or not
        for r in range(ROWS): 
            for c in range(COLS):
                if dfs(r, c, 0): 
                    return True
        
        return False
        