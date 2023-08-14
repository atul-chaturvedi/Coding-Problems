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
bool canSplitArray(vector<int>& nums, int m) {
    if(nums.size() <= 2) return true;
    for(int i = 1; i < nums.size(); i++){
        if(nums[i] + nums[i-1] >= m) return true;
    }
    return false;
}
    
};