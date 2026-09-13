class Solution:
    def maxIncreaseKeepingSkyline(self, grid: List[List[int]]) -> int:   
        n = len(grid)  
        row_max = [] 
        col_max = []  
        max_height_increase = 0 
        for i in range(n):
            row_max.append(max(grid[i]))

        i = 0
        while i < n:
            col_ele = []
            for j in range(n):
                col_ele.append(grid[j][i])
            i += 1
            col_max.append(max(col_ele))
            
        for i in range(n):
            for j in range(n):
                if grid[i][j] >= min(row_max[i], col_max[j]):
                    continue
                else:
                    max_height_increase = max_height_increase + (min(row_max[i], col_max[j]) - grid[i][j])
        return max_height_increase