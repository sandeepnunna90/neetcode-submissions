class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        cols = collections.defaultdict(set)
        rows = collections.defaultdict(set)
        squares = collections.defaultdict(set) # { r/3, c/3} the key here is tuple to identify the square { (0, 0): {'1', '5' ..}

        for r in range(9):
            for c in range(9): 
                if board[r][c] == ".": # The way this if condition is that we are actually iterating the board into an empty sudoku board with 9 x 9 grid - for my understanding, the if condition when our board is being filled)
                    continue
                
                if (board[r][c] in rows[r] or board[r][c] in cols[c] or board[r][c] in squares[(r // 3, c // 3)]): 
                    return False
                
                rows[r].add(board[r][c]) # adding to the set -> { 1: {1, 2, 3 ....}} adding a value to set(which value of hash)           
                cols[c].add(board[r][c]) # adding to the set -> { 1: {1, 2, 3 ....}} adding a value to set(which value of hash)           
                squares[(r // 3, c // 3)].add(board[r][c])
        return True
