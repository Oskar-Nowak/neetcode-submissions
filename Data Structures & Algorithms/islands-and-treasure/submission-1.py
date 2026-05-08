class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        INF = 2147483647
        directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
        rows, cols = len(grid), len(grid[0])

        q = collections.deque()

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 0:
                    q.append((r, c, 0))

        while q:
            r, c, dist = q.popleft()
            for d in directions:
                rd, cd = r + d[0], c + d[1]
                if (rd in range(rows) and
                    cd in range(cols) and
                    grid[rd][cd] != -1):

                    if grid[rd][cd] == INF:
                        grid[rd][cd] = dist + 1
                        q.append((rd, cd, dist + 1))