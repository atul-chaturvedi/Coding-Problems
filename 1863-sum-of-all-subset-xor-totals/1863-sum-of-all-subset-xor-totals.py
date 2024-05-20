class Solution:
    def __init__(self):
        self.list_subset = []
    def all_subset(self,curr_subset, index, nums):
        if index >= len(nums):
            return
        
        # global all_subset
        self.list_subset.append(curr_subset)
        
        self.all_subset(curr_subset[:], index+1, nums)
        curr_subset.append(nums[index])
        self.all_subset(curr_subset[:], index+1, nums)
        
    
    def subsetXORSum(self, nums: List[int]) -> int:
        self.all_subset([],0,nums)
        xor_sum =0
        for subset in self.list_subset:
            curr_xor  =0
            for num in subset:
                curr_xor = curr_xor ^ num
            
            xor_sum += curr_xor
                
            

        return xor_sum

    
        