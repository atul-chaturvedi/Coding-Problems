class Solution {
public:
    int maximumSafenessFactor(vector<vector<int>>& grid) {
        queue<array<int,2>> q;
        int n = grid.size();
        
        
         // it will make movement in four directions
        int dir[5] = {1, 0, -1, 0, 1};
        
        
        for(int i=0; i<n; i++){
            for(int j=0; j<n; j++){
                if(grid[i][j])
                    q.push({i,j});
            }
        }
        
        while(!q.empty()){
            auto [i,j] = q.front(); q.pop();
            
            // moving in left , right, top bottom directions
            for(int d=0; d<4; d++){
                int x = i + dir[d], y = j + dir[d+1];
                if(min(x,y) >=0  and  max(x,y) < n  and grid[x][y]  ==0 ){
                    grid[x][y]  = grid[i][j] +1;
                    q.push({x,y});
                } 
            }   
        }
        
        priority_queue<array<int, 3>> pq;
        pq.push({grid[0][0],0,0});
        // grid[0][0]
        
        while(pq.top()[1] <  n-1 || pq.top()[2] < n-1){
            auto [sf, i, j] = pq.top(); pq.pop();
            
            for(int d =0; d<4; d++){
                int x = i+ dir[d], y = j + dir[d+1];
                if(min(x,y) >=0 and max(x,y) < n and grid[x][y] !=-1){
                    pq.push({min(sf,grid[x][y]), x, y});
                    grid[x][y] = -1;
                }
            }
        }
        
        
        return pq.top()[0] -1;
        // return 10;
        
    }
};




// class Solution {
// public:
    
//     struct VectorHasher {
//         int operator()(const vector<int> &V) const {
//             int hash = V.size();
//             for(auto &i : V) {
//                 hash ^= i + 0x9e3779b9 + (hash << 6) + (hash >> 2);
//             }
//             return hash;
//         }
//     };
    
//     int final_score;
//     int n, m;
//     vector<pair<int,int>> theifs;
//     unordered_map<vector<int>, bool, VectorHasher> dpp;
    
//     void help(vector<vector<int>>& grid, int r, int c, int curr_score){
//         if(r < 0 || c < 0 || r >= n || c>= m || grid[r][c]==1)
//             return;
        
//         if(dpp.find({r, c, curr_score}) != dpp.end()){
//             return;
//         } 

        
//         int score = INT_MAX;
//         for(auto th: theifs){
//             score = min(score , abs(th.first - r) + abs(th.second - c));
//         }
        
//         curr_score = min(score, curr_score);
        
//         if(r==n-1 and c==n-1){
//             final_score = max(final_score, curr_score);
//             return;
//         }

        
        
//          grid[r][c] =1;
        
//         dpp[{r,c, curr_score}] = true;
         
        
//         help(grid, r+1, c, curr_score);
//         help(grid, r, c+1, curr_score);
//         help(grid, r-1, c, curr_score);
//         help(grid, r, c-1, curr_score);
        
//         grid[r][c] = 0;
        
//     }
//     int maximumSafenessFactor(vector<vector<int>>& grid) {
//         n = grid.size();
//         m = grid[0].size();
        
        
        
//         if(grid[0][0] == 1 || grid[n-1][m-1]==1)
//             return 0;
        
//         for(int i=0; i<n; i++){
//             for(int j =0; j<m; j++){
//                 if(grid[i][j]==1){
//                     theifs.push_back({i,j});
//                 }
//             }
//         }
        
//         final_score = 0;
//         help(grid, 0, 0, INT_MAX);
            
//         return final_score;
//     }
// };