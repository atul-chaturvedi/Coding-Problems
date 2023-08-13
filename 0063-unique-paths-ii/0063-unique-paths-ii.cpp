class Solution {
public:
    // int ans;
    int n, m;
    vector<vector<int>> dp;
    int help(vector<vector<int>>& g, int r, int c){
        if(r==n-1 and c==m-1){
            // ans = ans+1;
            return 1;
        }
        
        if(r < 0 || c < 0 || r>=n || c>=m|| g[r][c] == 1)
            return 0;
        
        if(dp[r][c] !=-1)
            return dp[r][c];
        
        g[r][c] =1;
        int currPath = help(g, r+1,c) + help(g, r, c+1);
        g[r][c] =0;
        
        dp[r][c] = currPath;
        return dp[r][c];
    }
    int uniquePathsWithObstacles(vector<vector<int>>& g) {
        n = g.size();
        m = g[0].size();
        if(g[0][0] || g[n-1][m-1])
            return 0;
        
        dp.resize(n, vector<int>(m,-1));
        int ans = help(g, 0, 0);
        return ans;
        
    }
};