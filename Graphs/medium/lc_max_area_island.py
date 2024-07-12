# https://leetcode.com/problems/max-area-of-island/
# m x n binary matrix grid
# 1 is land
# 0 is water
# edges of the grid are assumed to be surrounded by water
# Return the size of the bigest island
# Islands are formed 4-directionally



from collections import deque
from typing import List


class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        LAND, WATER = 1, 0

        max_island_size = 0

        def sunk_island(start):
            sunk_island_size = 0
            start_r, start_c = start
            q = deque()
            q.appendleft((start_r, start_c))
            # sink the island cell to prevent going in circles ('visited' in bfs)
            grid[start_r][start_c] = 0
            sunk_island_size += 1

            while q:
                r, c = q.pop()
                for dr, dc in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                    r_new, c_new = r + dr, c + dc
                    if r_new in range(0, ROWS) and c_new in range(0, COLS) and grid[r_new][c_new] == LAND:
                        grid[r_new][c_new] = 0
                        sunk_island_size += 1
                        q.appendleft((r_new, c_new))
            return sunk_island_size

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == LAND:
                    sunk_island_size = sunk_island((r,c))
                    max_island_size = max(sunk_island_size, max_island_size)
        return max_island_size


# Runtime: O(n * m)
# Space: O(1)
