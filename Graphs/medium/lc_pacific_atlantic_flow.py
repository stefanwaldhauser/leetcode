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
# BFS on each of the n * m fields. For each n * m field in the worst case we visit the other n &m fields, so
# O((ROWS * COLS) ** 2)



# Idea: Start with the cells bording the ocears and go 'reverse', find those cells that can reach the ocean bordering cells
class BetterSolution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        ROWS, COLS = len(heights), len(heights[0])
        pac, atl = set(), set()

        def dfs(r, c, visit, prevHeight):
            if ((r,c) in visit or r < 0 or c < 0 or r >= ROWS or c >= COLS or heights[r][c] < prevHeight):
                return
            # Found a new cell we can reach
            visit.add((r,c))
            dfs(r + 1,c, visit, heights[r][c])
            dfs(r - 1,c, visit, heights[r][c])
            dfs(r,c + 1, visit, heights[r][c])
            dfs(r,c - 1, visit, heights[r][c])

        for c in range(COLS):
            dfs(0, c, pac, heights[0][c])
            dfs(ROWS-1, c, atl, heights[ROWS-1][c])

        for r in range(ROWS):
            dfs(r, 0, pac, heights[r][0])
            dfs(r, COLS-1, atl, heights[r][COLS-1])

        res = []
        for r in range(ROWS):
            for c in range(COLS):
                if (r,c) in pac and (r,c) in atl:
                    res.append([r,c])
        return res

# Runtime: Per ocean we can visit a cell now once so per ocean O(ROWS * COLS) and then the final loop so O(ROWS * COLS * 3) = O(ROWS * COLS)

class Solution2:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        # Fact we can use: If water can flow into an ocean from cell x, than any cell y that flows into cell x can also flow into the ocean
        # We know the cells that border the oceans can flow into them
        # So all we do is to look for cells to flow to these ocean bordering cell by starting from
        # them and going backwards.
        # Imagine now we have a border cell x and discovered the whole graph of nodes that flow into x by going backwards. If we know investigate the graph of another border cell y, if we hit a cell of the already known graph, we dont have to continue as we would traverse the same route again. So what we basically need is a visited set that spans  multiple start nodes
        # Much more efficient than going from the inside outside. Imagine a map where the border cells are surrounded by very steep cells and nothing can flow into the border cells. If we start from the border cells we dont waste a lot of performance investigating the inside cells that can never reach the oceans
        ROWS, COLS = len(heights), len(heights[0])

        pacific_visited = set()
        atlantic_visited = set()

        def dfs(r, c, visited, last_height):
            if r >= 0 and r <= ROWS-1 and c >= 0 and c <= COLS-1 and (r,c) not in visited and last_height <= heights[r][c]:
                current_height = heights[r][c]
                visited.add((r,c))
                dfs(r-1,c,visited, current_height)
                dfs(r+1,c,visited, current_height)
                dfs(r,c-1,visited, current_height)
                dfs(r,c+1,visited, current_height)
                return
            else:
                return

        for c in range(COLS):
            dfs(0, c, pacific_visited, -1)
            dfs(ROWS-1, c, atlantic_visited, -1)
        for r in range(ROWS):
            dfs(r, 0, pacific_visited, -1)
            dfs(r, COLS-1, atlantic_visited, -1)

        intersection = pacific_visited.intersection(atlantic_visited)
        solutions = []
        for sol in intersection:
            (r, c) = sol
            solutions.append([r,c])
        return solutions
