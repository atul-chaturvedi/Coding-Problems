class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        ans =  []
        mp = {}
        for num in nums:
            if num in mp:
                mp[num] +=1
                ans.append(num)
            else:
                mp[num]  =1
                
        return ans
            
            