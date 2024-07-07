# https://leetcode.com/problems/rotting-oranges/
# m x n grid wher 1 <= m, n <= 10
# Each cell as one of three values 0, 1, 2
# 0 => empty cel
# 1 => fresh orange
# 2 => rotten orange

from collections import deque


class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        rotten = []
        fresh_count = 0

        for r in range(ROWS):
            for c in range(COLS):
                val = grid[r][c]
                if val == 1:
                    fresh_count += 1
                if val == 2:
                    rotten.append((r,c))

        minutes_passed = 0

        # We dont even need a visited ds here, we can just use the grid value of '2' as visited!
        q = deque()
        # Multiple Start Node BFS
        for rotten_orange in rotten:
            q.append(rotten_orange)
            # rotten oranges start cells are already at '2' so visited!

        while q and fresh_count > 0:
            # We need to remember when our bfs has worked through one layer to update the minutes
            for _ in range(len(q)):
                (_r,_c) = q.popleft()
                for dr, dc in [[-1, 0], [1,0], [0, 1], [0,-1]]:
                    r, c = _r + dr, _c + dc
                    # grid[r][c] == 1 means unvisited!
                    if r in range(0, ROWS) and c in range(0, COLS) and (r,c) and grid[r][c] == 1:
                        fresh_count -= 1
                        grid[r][c] = 2
                        q.append((r,c))
            minutes_passed += 1

        if fresh_count == 0:
            return minutes_passed
        return -1


# Runtime: Running BFS visits each node no matter what start node, so O(rows * cols).
