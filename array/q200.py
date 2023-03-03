from typing import List

# https://leetcode.com/problems/number-of-islands/

def numIslands(grid: List[List[str]]) -> int:
    '''
    Iterate from start to end of grid, where we trigger a floodfill
    method to change existing lands to water and adding to the island count.
    '''
    
    def floodfill(x: int, y: int, grid: List[List[str]]) -> List[List[str]]:
        '''
        Takes in a coordinate (x, y) and applies floodfill starting from the provided coordinates
        in the grid and expanding out until no lands ("1") could be modified to water ("0").
        '''

        grid[y][x] = "0"
        if y > 0 and grid[y-1][x] == "1":
            grid = floodfill(x, y-1, grid)
        if y < len(grid)-1 and grid[y+1][x] == "1":
            grid = floodfill(x, y+1, grid)
        if x > 0 and grid[y][x-1] == "1":
            grid = floodfill(x-1, y, grid)
        if x < len(grid[y])-1 and grid[y][x+1] == "1":
            grid = floodfill(x+1, y, grid)

        return grid
            
    num_of_islands = 0
    
    for y in range(len(grid)):
        for x in range(len(grid[y])):
            if grid[y][x] == "1":
                grid = floodfill(x, y, grid)
                num_of_islands += 1
                
    return num_of_islands

