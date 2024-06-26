# https://leetcode.com/problems/number-of-islands/description/



# m x n where 1 <= m, n <= 300
# grid[i][j] is '0' or '1'. 0 is water, 1 is land
# m == grid.length
# n == grid[i].length

import collections
from typing import List


class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0
        x_length = len(grid)
        y_length = len(grid[0])
        visited = set()
        islands = 0

        # We can think of a 2d array as an implicit representation of a graph
        # Each cell is a vertx with up to four edges connecting it to its neighbirs
        # Corners have two edges, Sides have three edges, Cells in the middle have all 4 edges
        def bfs(x,y):
            q = collections.deque()
            visited.add((x,y))
            q.append((x,y))

            while q:
                (_x, _y) = q.popleft() # just change to .pop to make it a iterative dfs
                # to find the neighbors we have to check each direction if its inside of the grid
                # right, left, up, down
                directions = [[1,0], [-1,0], [0,1], [0, -1]]

                for dx, dy in directions:
                    new_x = _x + dx
                    new_y = _y + dy
                    if new_x >= 0 and new_x < x_length and new_y >= 0 and new_y < y_length and grid[new_x][new_y] == '1' and (new_x, new_y) not in visited:
                        q.append((new_x,new_y))
                        visited.add((new_x, new_y))


        # We basically run a bfs on each 'new' island cell we see to discover the whole island
        for x in range(x_length):
            for y in range(y_length):
                if grid[x][y] == "1" and (x,y) not in visited:
                    bfs(x,y)
                    islands += 1
        return islands


# BFS is initiated for each unvisited land cell ('1').
# In the worst case, BFS visits all the cells in the grid m x n, but each cell is added to the queue and processed at most once.
# The BFS processes each cell and its neighbors, which translates to an amortized time of O(1)O(1) per cell since each cell is visited once.
# The overall runtime complexity is O(m×n)

# A set is used to keep track of visited cells, which could contain all cells in the worst case. The maximum size of the queue can be O(min⁡(m,n)) in the worst case of BFS, but it’s also bounded by the number of cells,
# The overall space complexity is O(m×n) due to the visited set and the BFS queue.
