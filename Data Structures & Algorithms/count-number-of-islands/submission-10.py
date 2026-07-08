class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid: 
            return 0
        islands = 0
        rows = len(grid)
        cols = len(grid[0])
        visit = set() #we want to track the 1s that we've visited
        # that way we don't necessarily increment the number of islands if we're visiting a 1 that's 
        # already been visited, this is the core logic of this algorithm
        # the rest is just breath first search that uses queues --> first in first out

        def bfs(r,c):
            directions = [[0,1],[0,-1],[1,0], [-1,0]]
            queue = collections.deque()
            queue.append((r,c))
            while queue:
                row, col = queue.popleft()
                for dr, dc in directions: 
                    r = row + dr
                    c = col + dc 
                    if (r in range(rows) and 
                        c in range(cols) and 
                        grid[r][c]=="1"  and 
                        (r,c) not in visit):

                        visit.add((r,c))
                        queue.append((r,c))
            


        for r in range(rows):
            for c in range(cols):
                if grid[r][c]=="1" and (r,c) not in visit:
                    bfs(r,c)
                    islands+=1

        return islands