class Solution {
public:
    vector<int> majorityElement(vector<int>& nums) {
        map<long long, int> count;
        int n = nums.size();
        vector<int> ans;
        for(int num: nums){
            count[num]++;
        }
        
        for(auto c: count){
            if (c.second > n/3 ){
                ans.push_back(c.first);
            }
        }
        
        return ans;
    }
};