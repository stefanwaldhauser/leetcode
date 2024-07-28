# m * n board where 1 <= m, n <= 6
# string word where 1 <= word.length <= 15
# return true if the word can be constructed in side of the board from letter horizontally or vertically neighboring
# ! THE SAME LETTER CELL MAY NOT BE USED MORE THAN ONCE!!!!


from typing import List


class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        ROWS, COLS = len(board), len(board[0])

        def backtrack(row, col, i):
            # Check if positive base case is reached
            if i == len(word):
                return True # have built the whole word, so we are one index past it
            # Check if negative base case is reached (made an invalid choice)
            if (row < 0 or row >= ROWS or
                col < 0 or col >= COLS or
                board[row][col] != word[i]):
                return False
            # Current choice valid -> perform choices of decision tree
            temp = board[row][col]
            board[row][col] = '#'  # mark as visited (Allows us to check in O(1) what we have visited)

            word_can_be_built = False
            for dr, dc in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
                word_can_be_built = backtrack(row + dr, col + dc, i+1)
                if word_can_be_built:
                    break
            board[row][col] = temp
            return word_can_be_built # True if any of the choices lead to the word being built, or False otherwise

        for r in range(ROWS):
            for c in range(COLS):
                word_can_be_built = backtrack(r, c, 0)
                if word_can_be_built:
                    return True
        return False
