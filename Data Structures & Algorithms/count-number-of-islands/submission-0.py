class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:

        if not grid:
            return 0
            
        islands = 0
        rows, columns = len(grid), len(grid[0])

        def dfs(r,c): #r,c is the specifc coordinate ur at
            if r<0 or r>=rows or c<0 or c>= columns  or grid[r][c] == "0": #bounds/not an island
                return #return nothing since out of bounds
            
            grid[r][c] = "0" #NOW we set this point to 0 since once we've visited it, (and even if its an island, we set to 0 so we dont revisit it and count it again)

            dfs(r+1, c) #now, dfs on all horizonal or vertical sides of the original coordinate
            dfs(r-1, c)
            dfs(r, c+1)
            dfs(r, c-1)

        
        for r in range(rows):
            for c in range(columns):
                if grid[r][c] == "1":
                    islands +=1
                    dfs(r,c)
        return islands

        