from collections import deque
from typing import List


class Solution:
    def wallsAndGates(self, rooms: List[List[int]]) -> None:
        """
        Do not return anything, modify rooms in-place instead.
        """
        EMPTY, GATE, WALL = 2147483647, 0, -1
        ROWS, COLS = len(rooms), len(rooms[0])
        layer = 0
        # 'visited' is just cells that are not EMPTY
        q = deque()
        # multi start bfs with gates as start points
        for r in range(ROWS):
            for c in range(COLS):
                if rooms[r][c] == GATE:
                    q.appendleft((r,c))

        while q:
            layer += 1
            for _ in range(len(q)):
                r,c = q.pop()
                for dr, dc in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                    r_new, c_new = r + dr, c + dc
                    if r_new in range(0, ROWS) and c_new in range(0, COLS) and rooms[r_new][c_new] == EMPTY:
                        rooms[r_new][c_new] = layer
                        q.appendleft((r_new, c_new))

# Runtime: O(n x m) for the BFS
# Space: O(1)
