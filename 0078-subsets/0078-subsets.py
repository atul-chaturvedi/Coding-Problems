class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        ans = []
        def recursion(curr_list, i):
            if i >= len(nums):
                ans.append(curr_list[:])
                return
            
            recursion(curr_list[:], i+1)
            curr_list.append(nums[i])
            recursion(curr_list[:], i+1)
            
        
        recursion([], 0)
        
        return ans
        