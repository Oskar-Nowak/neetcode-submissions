class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        if not grid:
            return 0

        rows, cols = len(grid), len(grid[0])
        max_area = 0

        def bfs(r: int, c: int) -> int:
            directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
            q = collections.deque()
            island_area = 1
            grid[r][c] = 0
            q.append((r, c))

            while q:
                row, col = q.popleft()
                for dr, dc in directions:
                    new_row, new_col = row + dr, col + dc
                    if (new_row in range(rows) and
                        new_col in range(cols) and
                        grid[new_row][new_col] == 1):
                        island_area += 1
                        grid[new_row][new_col] = 0
                        q.append((new_row, new_col))
            return island_area

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    max_area = max(max_area, bfs(r, c))

        return max_area