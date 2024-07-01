# heights 2d array where 1 <= columns, rows <= 100
# 0 <= heights[r][c] <= 1000

# heights[r][c] is height above see level at (r, c)
# Water can flow in four directiosn up, down, left, right if the height of the target neighbor cell is equal or lower
# Water can flow always outside of the grid (basically level 0 all around)

# Find all cells where a water drop that falls on this cell will flow to BOTH the Pacific and Atlantic ocean. Return [] if not possible
# Return as a 2D list where each elements [[r1,c2], [r2,c2]] and so on of the respective cells in any order

from collections import deque


class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        # [r,c] will be 1 if it is a solution cell
        no_rows = len(heights)
        no_cols = len(heights[0])
        cell_info = []
        for i in range(no_rows):
            row = []
            for j in range(no_cols):
                row.append(0)
            cell_info.append(row)

        def investigate_cell(start):
            (start_r, start_c) = start
            visited = set()
            q = deque()
            flows_into_pacific = False
            flows_into_atlantic = False

            visited.add((start_r,start_c))
            q.append((start_r,start_c))

            while q:
                (_r, _c) = q.popleft()

                # if we hit a cell that is already a solution we can stop early as we will definitely hit both oceans
                if cell_info[_r][_c] == 1:
                    cell_info[start_r][start_c] = 1
                    return


                if _r == 0 or _c == 0:
                    flows_into_pacific = True

                if _r == no_rows -1 or _c == no_cols -1:
                    flows_into_atlantic = True


                directions = [[1,0], [-1,0], [0,1], [0, -1]]

                for dr, dc in directions:
                    new_r = _r + dr
                    new_c = _c + dc
                    if new_r >= 0 and new_r < no_rows and new_c >= 0 and new_c < no_cols and (new_r, new_c) not in visited and heights[_r][_c] >= heights[new_r][new_c]:
                        q.append((new_r,new_c))
                        visited.add((new_r, new_c))

                if flows_into_pacific == True and flows_into_atlantic == True:
                    cell_info[start_r][start_c] = 1

        for r in range(no_rows):
            for c in range(no_cols):
                investigate_cell((r,c))

        solution = []
        for r in range(no_rows):
            for c in range(no_cols):
                if cell_info[r][c] == 1:
                    solution.append([r,c])
        return solution

# Correct but brute force (even with the small improvement), really bad runtime
