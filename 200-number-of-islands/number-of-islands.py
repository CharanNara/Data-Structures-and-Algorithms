class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        directions = [[0,1],[1,0],[0,-1],[-1,0]]
        rows, cols = len(grid), len(grid[0])

        # from one position you explore all possible directions where island is connected

        visited = set()

        def explore(r, c):
            if (r, c) in visited:
                return
            visited.add((r,c))

            for dr,dc in directions:
                nr, nc = dr+r, dc+c

                if nr in range(rows) and nc in range(cols) and (nr, nc) not in visited and grid[nr][nc] == "1":
                    explore(nr, nc)


        res = 0

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == "1" and (r, c) not in visited:
                    explore(r, c)
                    res += 1
        return res