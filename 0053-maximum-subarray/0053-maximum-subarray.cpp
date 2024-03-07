class Solution {
public:
    int maxSubArray(vector<int>& nums) {
        int curr_sum = nums[0];
        int max_sum = nums[0];
        int n = nums.size();
        
        for(int i=1; i<n; i++){
            curr_sum = max(curr_sum+nums[i], nums[i]);
            max_sum = max(curr_sum, max_sum);
        }
        
        return max_sum;
    }
};