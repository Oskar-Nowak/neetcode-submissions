class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        directions = [[1,0],[-1,0],[0,1],[0,-1]]
        rows, cols = len(grid), len(grid[0])

        queue = collections.deque()
        
        fresh_count = 0

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    fresh_count += 1
                if grid[r][c] == 2:
                    queue.append((r, c))
        if fresh_count == 0:
            return 0

        time = 0
        while queue and fresh_count > 0:
            time += 1
            for _ in range(len(queue)):
                r, c = queue.popleft()
                for d in directions:
                    rd, cd = r + d[0], c + d[1]

                    if (rd in range(rows) and 
                        cd in range(cols) and
                        grid[rd][cd] == 1):
                        grid[rd][cd] = 2
                        fresh_count -= 1
                        queue.append((rd, cd))

        return time if fresh_count == 0 else -1
