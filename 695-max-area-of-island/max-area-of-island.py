class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        
        # to get max area we explore wherever we encounter a land and keep exploring

        rows, cols = len(grid), len(grid[0])
        directions = [[0,1],[1,0],[0,-1],[-1,0]]

        visited=set()

        def explore(r, c):
            if (r,c) in visited:
                return 0
            visited.add((r,c))
            area = 1

            for dr, dc in directions:
                nr, nc = dr+r, dc+c

                if nr in range(rows) and nc in range(cols) and (nr, nc) not in visited and grid[nr][nc] == 1:
                    area += explore(nr, nc)
            
            return area

        max_area = float('-inf')
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1 and (r,c) not in visited:
                    max_area = max(max_area, explore(r,c))
        return max_area if max_area != float('-inf') else 0
