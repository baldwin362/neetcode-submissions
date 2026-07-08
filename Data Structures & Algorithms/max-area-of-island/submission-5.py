class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:

        if not grid:
            return 0

        directions = [[0,1], [0,-1], [1,0],[-1,0]]
        visit = set()
        rows = len(grid)
        cols = len(grid[0])
        max_area = 0

        def bfs(r,c)->int:
            q = collections.deque()
            q.append((r,c))
            visit.add((r,c))
            new_area = 1
            while q:
                row,col = q.popleft()
                for dr,dc in directions:
                    nr = row + dr
                    nc = col + dc 
                    if (nr in range(rows) and
                        nc in range(cols) and 
                        grid[nr][nc]==1 and 
                        (nr,nc) not in visit):
                        q.append((nr,nc))
                        visit.add((nr,nc))
                        new_area += 1
            return new_area

        for r in range(rows):
            for c in range(cols):
                if grid[r][c]==1 and (r,c) not in visit:
                    new_area = bfs(r,c)
                    if new_area > max_area: 
                        max_area = new_area

        return max_area