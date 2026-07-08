class Solution:
    def countPaths(self, grid: List[List[int]]) -> int:
        visit = set()
        return self.countPathsHelper(grid, 0, 0, visit)
    def countPathsHelper(self, grid, r,c,visit) -> int:
        rows = len(grid)
        cols = len(grid[0])
        if min(r,c) < 0 or r==rows or c==cols or grid[r][c]==1 or (r,c) in visit:
            return 0
        if r==rows-1 and c==cols-1:
            return 1
        visit.add((r,c))
        count = 0
        count += self.countPathsHelper(grid,r,c+1,visit) 
        count += self.countPathsHelper(grid,r,c-1,visit)
        count += self.countPathsHelper(grid,r-1,c,visit)
        count += self.countPathsHelper(grid,r+1,c,visit)
        visit.remove((r,c))

        return count
        

