class Solution:
    def findMaxK(self, nums: List[int]) -> int:
        nums = set(nums)
        nums = list(nums)
        nums.sort()
        left = 0
        right = len(nums)-1
        
       
        
        while left < right:
            if abs(nums[left]) == abs(nums[right]):
                return abs(nums[left])
            elif abs(nums[left]) > abs(nums[right]):
                left+=1
                
            else:
                right-=1
                
        
        return -1
                
                