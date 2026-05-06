class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0

        rows, cols = len(grid), len(grid[0])
        islands = 0

        def bfs(row: int, col: int):
            directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
            q = collections.deque()
            grid[row][col] = '0'
            q.append((row, col))

            while q:
                r, c = q.popleft()
                for dr, dc in directions:
                    if (r + dr in range(rows) and
                        c + dc in range(cols) and
                        grid[r + dr][c + dc] == "1"):
                        grid[r + dr][c + dc] = "0"
                        q.append((r + dr, c + dc))

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == '1':
                    bfs(r, c)
                    islands += 1
        
        return islands