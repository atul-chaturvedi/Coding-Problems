class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        ans = []
        def dfs(curr_comb, curr_sum, i):
            if curr_sum == target:
                ans.append(curr_comb[:])
                
            if i >= len(candidates):
                return 

            
            if curr_sum > target:
                return
            
            for j in range(i, len(candidates)):
                dfs(curr_comb[:] + [candidates[j]], curr_sum +candidates[j], j)
            
        dfs([],0,0)
    
        return ans
            
        