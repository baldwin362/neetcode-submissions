class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid: 
            return 0
        rows = len(grid)
        cols = len(grid[0])
        visit = set() #sorted hash 
        islands = 0
        directions = [[0,1],[0,-1],[1,0],[-1,0]]
        
        def bfs(r:int,c:int) -> None:
            q = collections.deque()
            visit.add((r,c))
            q.append((r,c))
            while q:
                row, col = q.popleft() #LIFO: Last in First out 
                for dr,dc in directions:
                    nr = row + dr 
                    nc = col + dc 

                    if (nr in range(rows) and 
                    nc in range(cols) and 
                    grid[nr][nc]=="1" and 
                    (nr,nc) not in visit):
                        visit.add((nr,nc))
                        q.append((nr,nc))
            

        for r in range(rows):
            for c in range(cols): 
                if grid[r][c] == "1" and (r,c) not in visit: 
                    bfs(r,c)
                    islands +=1
        return islands