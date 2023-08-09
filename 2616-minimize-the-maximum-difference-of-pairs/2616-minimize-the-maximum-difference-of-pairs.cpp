class Solution {
public:
    int minimizeMax(vector<int>& nums, int p) {
        int n = nums.size();
        sort(nums.begin(), nums.end());
        int left = 0, right = nums[n-1] - nums[0];
        
        while(left <right){
            int mid = left  + (right - left)/2;
            
            int count = 0;
            for(int i=1; i<n; i++){
                if(abs(nums[i-1] - nums[i]) <= mid){
                    count++;
                    i++;
                }
            }
            
            if(count >= p)
                right = mid;
            else
                left = mid + 1;
        }
        
        return left;

    }
    
};



  



    

   
      
    