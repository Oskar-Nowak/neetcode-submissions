class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        rows, cols = len(grid), len(grid[0])

        def bfs(row, col):
            directions = [[1,0],[-1,0],[0,1],[0,-1]]
            q = collections.deque()

            q.append((row, col, 0))
            visited = set()
            visited.add((row, col))

            while q:
                r, c, dist = q.popleft()
                for direction in directions:
                    rd, cd = r + direction[0], c + direction[1]

                    if (rd in range(rows) and
                        cd in range(cols) and
                        (rd, cd) not in visited and
                        grid[rd][cd] != -1):

                        if grid[rd][cd] == 0:
                            grid[row][col] = dist + 1
                            return
                    
                        visited.add((rd, cd))
                        q.append((rd, cd, dist + 1))
                    
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == -1 or grid[r][c] == 0:
                    continue
                bfs(r, c)