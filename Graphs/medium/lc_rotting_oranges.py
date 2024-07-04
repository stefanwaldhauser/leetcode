# https://leetcode.com/problems/rotting-oranges/
# m x n grid wher 1 <= m, n <= 10
# Each cell as one of three values 0, 1, 2
# 0 => empty cel
# 1 => fresh orange
# 2 => rotten orange

# Every minute a fresh orange that becomes 4-directionally adjacent to a rotten orang becomes rotten
#  eturn the minimum number of minutes that must elapse until no cell has a fresh orange. If this is impossible, return -1.


# Solution is multi source BFS. We just need to initialise our Q with all the initial rotten oranges
# to represent the first 'layer'
# Time complexity O(n *m) going to visit all cells once and space complexity als O(n * m)
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        q = deque()
        layer, fresh = 0,0
        ROWS, COLS = len(grid), len(grid[0])

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 1:
                    fresh += 1
                if grid[r][c] == 2:
                    q.append([r,c])

        directions = [[0,1], [0,-1], [1,0], [-1, 0]]
        # We could have only one fresh orange and all rotten. Waste of performance if we would go through all of the rotten
        while q and fresh > 0:
            layer_size = len(q) # Number of nodes at the current layer

            # work through the current layer. We need to do this trick here to increment the layer count
            for _ in range(layer_size):
                r,c = q.popleft()
                for dr, dc in directions:
                    row, col = dr + r, dc + c
                    if row < 0 or row >= ROWS or col < 0 or col >= COLS or grid[row][col] != 1:
                        continue
                    grid[row][col] = 2 # make rotten
                    q.append([row, col])
                    fresh -= 1
            layer += 1

        return layer if fresh == 0 else -1
