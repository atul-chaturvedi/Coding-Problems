class Solution {
public:
//     unordered_map<string,int> dp;
//     bool help(vector<int>& nums, int lsize, int m){
        
//         int lsum =0, rsum =0;
//         string key = "";
//         vector<int> l,r;
//         for(int i=0; i<lsize; i++){
//             lsum += nums[i];
//             l.push_back(nums[i]);
//             key += to_string(nums[i]);
//         }
        
//         key = key +'-';
        
//         for(int i=lsize; i<nums.size(); i++){
//             rsum += nums[i];
//             r.push_back(nums[i]);
//             key += to_string(nums[i]);
//         }
        
//         if(dp.find(key) != dp.end())
//             return dp[key];
        
//         // cout<<l.size()<<" "<<r.size()<<" "<<lsum<<" "<<rsum<<" "<<m<<"\n";
        
//         bool left = false;
//         bool right = false;
        
// //         for(int i=1; i<l.size(); i++){
// //             if(help(l,i,m))
// //                 left = true;
// //         }
        
        
// //         for(int j=1; j<r.size(); j++){
// //             if(help(r,j,m))
// //                 right = true;
// //         }
        
//         if(l.size() == 1 and r.size() == 1){
//             // cout<<"A ";
//             left = true;
//             right = true;
            
            
//         }
//         else if(l.size() == 1 and rsum >= m){
//             // cout<<"B ";
//             left = true;
//             for(int i=1; i<r.size(); i++)
//                 if(help(r,i,m))
//                 right = true;
            
//         }
//         else if(lsum >= m  and r.size() == 1 ){
//             // cout<<"C ";
//             right = true;
//             for(int i=1; i<l.size(); i++)
//                 if(help(l,i,m))
//                 left = true;
//         }
//         else if(rsum >= m and lsum >=m){
//             // cout<<"D ";
//             for(int i=1; i<l.size(); i++){
//                 if(help(l,i,m))
//                 left = true;
//             }
            
//             for(int i=1; i<r.size(); i++){
//                 if(help(r,i,m))
//                 right = true;
//             }
            
//         }
        
//         // cout<<"left = "<<left<<" "<<"right = "<<right<<"\n";
//         // cout<<"--------------------"<<"\n";
        
//         if(left and right)
//             dp[key] = 1;
//         else
//             dp[key] = 0;

//         return left and right;
        
//     }
    
//     bool canSplitArray(vector<int>& nums, int m) {
//         if(nums.size()==1)
//             return true;
//         bool ans = false;
//         for(int i=1; i<nums.size(); i++){
//             // dp.resize(nums.size()+1, vector<int>(nums.size(),-1));
//             if(help(nums, i, m))
//                 ans = true;
//         }
        
//         return ans;

//     }

    
// --------------------------------------------------Approch 1-----------------------------------------------
// Approach
// This case is only possible if there are two consecutive number whose sum is greater than or equal to m. Because if we have this case then we can simply remove all previous and post numbers one by one. But if this is not present then there is no way we can devide all the elements as at some point we arrive at point where we have three numbers left and non of the two consicutive sum greater than or equal to m.

// Note : corner case - if we have less and 2 elements then it is always possible to divide it into two as each have a length of 1.
// bool canSplitArray(vector<int>& nums, int m) {
//     if(nums.size() <= 2) return true;
//     for(int i = 1; i < nums.size(); i++){
//         if(nums[i] + nums[i-1] >= m) return true;
//     }
//     return false;
// }
    
    
// ---------------------------------------------------Approach 2---------------------------------------------------
// Intuition
//  -->We try to make partition at every index, if we can partition following the two conditions, rest recursion will handle.

// Approach
//  ->Partiton after each index, check if partition is correct (fulfills both the conditions)
// -->Check recursively on the two partitions made for the same conditions
// -->Apply memoization

    int dp[101][101];
    vector<int> prefixSum;
    int solve(int i, int j, vector<int>&nums, int m) {
        if (i == j) return 1;
        if (dp[i][j] != -1) return dp[i][j];

        int sum = 0;
        if (i == 0) sum = prefixSum[j];
        else sum = prefixSum[j] - prefixSum[i - 1];

        if (j - i == 1 && sum >= m) return dp[i][j] = 1;
        if (sum < m) return dp[i][j] = false;

        dp[i][j] = false;
        for (int k = i; k < j; k++) {
            if (solve(i, k, nums, m) == 1 && solve(k + 1, j, nums, m) == 1) {
                return dp[i][j] = (dp[i][j] || true);
            }
        }
        return dp[i][j];
    }

    bool canSplitArray(vector<int>& nums, int m) {
        int n = nums.size();
        memset(dp, -1, sizeof(dp));
        prefixSum.assign(n, 0);
        prefixSum[0] = nums[0];
        for (int i = 1; i < n; i++) {
            prefixSum[i] = prefixSum[i - 1] + nums[i];
        }
        if (n == 2) return true;
        return solve(0, n - 1, nums, m);
    }
};
    





