class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        max_prod = -10000000000
        curr_prod = 1
        
        for i in range(0, len(nums)):
            if curr_prod ==0:
                curr_prod =1
                
            curr_prod = curr_prod * nums[i]
            max_prod = max(curr_prod, max_prod)
            
        
        curr_prod =1
        for i in range(len(nums)-1, -1, -1):
            if curr_prod ==0:
                curr_prod =1
                
            curr_prod = curr_prod * nums[i]
            max_prod = max(curr_prod, max_prod)            
            
            

            
        return max_prod