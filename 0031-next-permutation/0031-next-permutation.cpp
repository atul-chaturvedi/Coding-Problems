class Solution {
public:
    void nextPermutation(vector<int>& nums) {
    // int n = nums.size();
    // if(n==1)
    //     return;
    // int j=0;
    // bool flag = false;
    // int count =0;
    // for(int i=0; i<n-1; i++){
    //     if(nums[i] > nums[i+1]){
    //         if(!flag)
    //             j =i;
    //         flag = true;
    //         count++;
    //     }
    // }
    // if(flag == false){
    //     cout<<"1";
    //     int temp = nums[n-1];
    //     nums[n-1] = nums[n-2];
    //     nums[n-2] = temp;
    //     return;
    // }
    // else if(count >=n-1){
    //     cout<<"2";
    //     sort(nums.begin(), nums.end());
    //     return;
    // }
    // else{ 
    //     cout<<"3";
    //     // auto min_element_pos = max_element(nums.begin()+j, nums.end());
    //     int index = nums.size();
    //     while(true){
    //         cout<<"j"<<j<<"\n";
    //         auto min_element_pos = upper_bound(nums.begin()+j, nums.end(), nums[j]);
    //         index = min_element_pos - nums.begin();
    //         if(index == nums.size()){
    //             j--;
    //         }else{
    //             break;
    //         }
    //     }
    //     cout<<index<<"\n";
    //     int temp = nums[j];
    //     nums[j] = nums[index];
    //     nums[index] = temp;
    //     // swap(nums[j], nums[index]);
    //     sort(nums.begin()+j, nums.end());
    //     return;
    // }
    int n = nums.size();
    int index = -1;
    for(int i= n-2; i>=0; i--){
        if(nums[i] < nums[i+1]){
            index = i;
            break;
        }
    }
    if(index ==-1){
        reverse(nums.begin(), nums.end());
        return;
    }
    
    for(int i=n-1; i>index; i--){
        if(nums[i] > nums[index]){
            swap(nums[i], nums[index]);
            break;
        }
    }
    
    reverse(nums.begin()+index+1, nums.end());
        
    
    return;
    
    }
};