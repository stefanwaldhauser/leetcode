class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:

        # You can apparently also calculate this by a formula see solution below
        def find_3x3(r, c):
            if r in range(0, 3):
                if c in range(0, 3):
                    return 0
                if c in range(3, 6):
                    return 1
                return 2
            if r in range(3, 6):
                if c in range(0, 3):
                    return 3
                if c in range(3, 6):
                    return 4
                return 5
            if c in range(0, 3):
                return 6
            if c in range(3, 6):
                return 7
            return 8

        row_count = [[0 for _ in range(9)] for _ in range(9)]
        col_count = [[0 for _ in range(9)] for _ in range(9)]
        c3x3_count = [[0 for _ in range(9)] for _ in range(9)]

        for r in range(9):
            for c in range(9):
                cell_value = board[r][c]

                if cell_value != ".":
                    cell_number = int(cell_value)
                    row_count[r][cell_number - 1] += 1
                    col_count[c][cell_number - 1] += 1
                    c3x3_count[find_3x3(r, c)][cell_number-1] += 1

                    if row_count[r][cell_number - 1] > 1 or col_count[c][cell_number - 1] > 1 or c3x3_count[find_3x3(r, c)][cell_number-1] > 1:
                        return False
        return True

# Time Complexity: O(n²)
# - Main nested loop iterates through every cell in the n x n board:
# - Outer loop: n iterations
# - Inner loop: n iterations
# - Total iterations: n * n
# - Inside the loop:
# - find_3x3 function is O(1)
# - Array accesses and comparisons are O(1)
# - All other operations are O(1)
# - Total runtime: O(n²)

# And for completeness:
# Time Complexity: O(n²)
# - The main loop iterates through every cell: n * n iterations
# - Each operation inside is O(1)
# - Total: O(n²)

#Better Solution
class BetterSolution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        cols = defaultdict(set) # Maps numbers to sets
        rows = defaultdict(set) # Maps numbers to sets
        squares = defaultdict(set) # Maps tuples to sets

        for r in range(9):
            for c in range(9):
                if board[r][c] == ".":
                    continue
                if (board[r][c] in rows[r]
                    or board[r][c] in cols[c]
                        or board[r][c] in squares[(r // 3, c // 3)]):
                    return False

                cols[c].add(board[r][c])
                rows[r].add(board[r][c])
                squares[(r // 3, c // 3)].add(board[r][c])

        return True
