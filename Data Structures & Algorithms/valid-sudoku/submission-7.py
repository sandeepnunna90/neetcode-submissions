class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        """
        Strategy: Scan every cell once (left-to-right, top-to-bottom).
        For each filled cell, check if its digit has already been seen
        in the SAME row, SAME column, or SAME 3x3 box. If yes -> duplicate
        found -> board is invalid. If we finish scanning with no duplicates,
        the board is valid.

        We use 3 dictionaries of sets to "remember" what's been seen so far:
            rows[r]                -> digits seen in row r
            cols[c]                -> digits seen in column c
            squares[(r//3, c//3)]  -> digits seen in that 3x3 box

        Why sets? Because we only care about MEMBERSHIP ("has this digit
        appeared here before?") -- not position or order. Sets give O(1)
        "in" checks, which is exactly what we need.

        ----------------------------------------------------------------
        WORKED EXAMPLE (partial board, only showing filled cells):

            board[0][0] = '5'
            board[0][1] = '3'
            board[1][0] = '6'
            board[4][4] = '4'

        After processing these 4 cells, the dictionaries look like:

            rows = {
                0: {'5', '3'},   # row 0 has seen digits 5 and 3
                1: {'6'},        # row 1 has seen digit 6
                4: {'4'},        # row 4 has seen digit 4
            }

            cols = {
                0: {'5', '6'},   # column 0 has seen digits 5 and 6
                1: {'3'},        # column 1 has seen digit 3
                4: {'4'},        # column 4 has seen digit 4
            }

            squares = {
                (0, 0): {'5', '3', '6'},   # top-left box saw 5, 3, 6
                (1, 1): {'4'},             # middle box saw 4
            }

        Note: (0,0)->0//3, 1//3 both map to box row/col 0, so cells
        (0,0), (0,1), (1,0) all land in the SAME box key (0,0), and
        their digits all pile into ONE shared set.

        Now suppose the next cell is board[1][1] = '5'.
            r, c = 1, 1  -> key = (1//3, 1//3) = (0, 0)
            Check: '5' in squares[(0,0)]?  -> {'5','3','6'} contains '5'
            -> TRUE -> duplicate found in the box -> return False
        ----------------------------------------------------------------
        """

        cols = collections.defaultdict(set)     # cols[c]    = set of digits seen in column c
        rows = collections.defaultdict(set)     # rows[r]    = set of digits seen in row r
        squares = collections.defaultdict(set)  # squares[(r//3, c//3)] = set of digits seen in that box

        for r in range(9):
            for c in range(9):
                # Skip empty cells -- nothing to validate, nothing to record
                if board[r][c] == ".":
                    continue

                val = board[r][c]

                # (r // 3, c // 3) collapses the 81 cells into 9 box-labels:
                #   r=0,1,2 -> 0 | r=3,4,5 -> 1 | r=6,7,8 -> 2   (box row)
                #   c=0,1,2 -> 0 | c=3,4,5 -> 1 | c=6,7,8 -> 2   (box col)
                # so all 9 cells physically inside the same 3x3 box
                # compute the SAME tuple key, and share the SAME set.
                box_key = (r // 3, c // 3)

                # CHECK FIRST (before adding): has this digit already
                # shown up in this row / this column / this box?
                if (val in rows[r] or val in cols[c] or val in squares[box_key]):
                    return False  # duplicate found -> invalid board

                # No conflict -- record this digit as "seen" in all three groups
                rows[r].add(val)
                cols[c].add(val)
                squares[box_key].add(val)

        # Scanned all 81 cells, no duplicates found in any row/col/box
        return True