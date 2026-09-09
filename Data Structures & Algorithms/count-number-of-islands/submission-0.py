class Solution:
    directions = [(0,-1), (0,1), (-1, 0), (1, 0)]

    def numIslands(self, grid: List[List[str]]) -> int:
        # dfs to find an island. Will return a set of coordinates that have been visited. 
        # increment num of islands
        # For each element in grid, check if it is not part of visited coordinates and is equal to 1, if so begin counting island. 

        def dfs(visited_coordinates, i, j):
            if i < 0 or j < 0 or i >= len(grid) or j >= len(grid[i]):
                return
 
            if grid[i][j] == '0' or ((i,j) in visited_coordinates):
                return
            
            visited_coordinates.add((i,j))
    
            for (x,y) in self.directions:
                dfs(visited_coordinates, i + x, j + y)

        coord = set()
        res = 0

        for i in range(0, len(grid)):
            for j in range(0, len(grid[i])):
                if grid[i][j] == '1' and ((i,j) not in coord):
                    res += 1
                    dfs(coord, i, j)
        
        return res



