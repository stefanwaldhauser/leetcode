# https://leetcode.com/problems/search-a-2d-matrix/description/
# n * m matrix where 1<= m, n <= 100
# Each row is sorted ascending 1, 3, 5, 7
# The next row begins with a larger number than the previous row ends
# Basically an ascending sorted list but wrapped in rows
# given an integer target, return true if target is in matrix or false otherwise


# ROWS, COLS
# each row r contains numbers n from          r[0] <= n <= r[COLS-1]

# Binary search in last column to find row that contains target O(log(ROWS))
# if its impossible to be in any row return false
# otherwise do binary search inside of the row to check if it exists O(log(COLS))


class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        ROWS, COLS = len(matrix), len(matrix[0])

        def possible_row():
            search_space_min = 0
            search_space_max = ROWS - 1

            while search_space_min < search_space_max:
                search_space_mid = (search_space_max - search_space_min) // 2 + search_space_min
                if target >= matrix[search_space_mid][0] and target <= matrix[search_space_mid][COLS-1]:
                    return search_space_mid
                elif target < matrix[search_space_mid][0]:
                    search_space_max = search_space_mid - 1
                else:
                    search_space_min = search_space_mid + 1
            if target >= matrix[search_space_min][0] and target <= matrix[search_space_min][COLS-1]:
                return search_space_min
            else:
                return -1


        def contained_in_row(row_number):
            row = matrix[row_number]

            search_space_min = 0
            search_space_max = len(row)

            while search_space_min < search_space_max:
                search_space_mid = (search_space_max - search_space_min) // 2 + search_space_min
                if row[search_space_mid] == target:
                    return True
                elif row[search_space_mid] < target:
                    search_space_min = search_space_mid + 1
                else:
                    search_space_max = search_space_mid -1
            return row[search_space_min] == target


        row_number = possible_row()
        if row_number == -1:
            return False
        else:
            return contained_in_row(row_number)


# Runtime: Finding row with binary search is O(log(ROWS)), looking into the row is O(log(COLS))
# By logarithm low O(log(ROWS)) + O(log(COLS)) = O(log(ROWS * COLS))
# Space: O(1)
