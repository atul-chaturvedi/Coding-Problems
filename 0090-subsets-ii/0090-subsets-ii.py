class Solution {
public:
    set<vector<int>> ans;
    void help(vector<int>& nums, int i, int n, vector<int> curr_subs){
        if(i>= n){
            ans.insert(curr_subs);
            return;
        }
        
        help(nums, i+1, n, curr_subs);
        curr_subs.push_back(nums[i]);
        help(nums, i+1, n, curr_subs);
        
        // 0 {}
        
    }
    vector<vector<int>> subsetsWithDup(vector<int>& nums) {
        sort(nums.begin(), nums.end());
        help(nums, 0, nums.size(), {});
        vector<vector<int>> fans(ans.begin(), ans.end());
        return fans;
    }
};