#EXTRA CREDIT

#64. Minimum Path Sum
class Solution:
    def minPathSum(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        Details 
        Runtime: 60 ms, faster than 65.57% of Python3 online submissions for Minimum Path Sum.
        """
        clength = len(grid[0])
        rlenght = len(grid)
        tc = [[0 for i in range(len(grid[0]))] for j in range(len(grid)) ]
        
        tc[0][0] = grid[0][0]
        #columns
        for x in range(1, rlenght):
            tc[x][0] = tc[x-1][0] + grid[x][0]
        #rows
        for y in range(1, clength):
            tc[0][y] = tc[0][y-1] + grid[0][y]
        #rest
        for r in range(1, rlenght):
            for c in range(1, clength):
                tc[r][c] = min(tc[r-1][c], tc[r][c-1]) + grid[r][c]
                       
        return tc[rlenght-1][clength-1]
        
    #120. Triangle        
    def minimumTotal(self, triangle):
        """
        :type triangle: List[List[int]]
        :rtype: int
        Details 
        Runtime: 84 ms, faster than 7.54% of Python3 online submissions for Triangle.
        """
        tlen = len(triangle)
        for i in range(1, tlen):
            for j in range(0, i+1):
                #
                if j ==0:
                    triangle[i][j] += triangle[i-1][j]
                elif j == i:
                    triangle[i][j] += triangle[i-1][j-1]
                else:
                    triangle[i][j] = triangle[i][j]+min(triangle[i-1][j-1], triangle[i-1][j])
                    
        return min(triangle[tlen-1])
        
