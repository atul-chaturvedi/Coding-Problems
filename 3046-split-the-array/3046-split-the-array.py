class Solution:
    def isPossibleToSplit(self, nums: List[int]) -> bool:
        hm = Counter(nums)
        
        for num in nums:
            if num in hm and hm[num] > 2:
                return False
            
        
        return True