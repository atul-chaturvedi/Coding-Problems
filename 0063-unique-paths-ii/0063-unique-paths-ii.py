class Solution:
    def uniquePathsWithObstacles(self, g: List[List[int]]) -> int:
        
        n = len(g)
        m = len(g[0])
        
        
        if g[0][0]==1 or g[n-1][m-1]==1:
            return 0
        
        dp = arr = [[-1 for j in range(m)] for i in range(n)]
        
        def help(r,c):
            if(r==n-1) and (c ==m-1):
                return 1
            
            if (r < 0) or (c < 0) or (r>=n) or (c>=m) or (g[r][c]==1):
                return 0
            
            if dp[r][c] != -1:
                return dp[r][c]
            
            # g[r][c] =1
            
            pathCount = help(r+1, c) + help(r,c+1)
            
            # g[r][c] = 0
            
            dp[r][c] = pathCount
            
            return dp[r][c]
        
        return help(0,0)