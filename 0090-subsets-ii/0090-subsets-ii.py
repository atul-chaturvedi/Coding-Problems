class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        ans = []
        curr_subset = []

        def findSubsets(i):
            if i>= len(nums):
                ans.append(curr_subset[:])
                return;
            
            # print(curr_subset)
            curr_subset.append(nums[i]);
            findSubsets(i+1)
            curr_subset.pop(-1)
            while(i+1  < len(nums) and nums[i] == nums[i+1]):
                i+=1
            
            findSubsets(i+1)
            
    

        findSubsets(0)

        return ans
        
    
    