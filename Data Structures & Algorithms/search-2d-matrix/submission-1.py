class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:

        ROWS, COLS = len(matrix), len(matrix[0])

        top, bot = 0, ROWS - 1

        rowIndex = 0

        while top <= bot:
            row = (top + bot) // 2 # middle row

            if target > matrix[row][-1]:
                top = row + 1
            elif target < matrix[row][0]:
                bot = row - 1
            else: 
                arr = matrix[row]
                l, r = 0, COLS - 1

                while l <= r:
                    mid = (l+r) // 2

                    if target > arr[mid]:
                        l = mid + 1
                    elif target < arr[mid]:
                        r = mid - 1
                    else:
                        return True
                return False
        return False
