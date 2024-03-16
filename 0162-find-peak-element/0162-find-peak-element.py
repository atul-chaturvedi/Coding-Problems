class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        # brute force approach
        index = -1
        max_element = -2147483649
        
        for i in range(len(nums)):
            if nums[i] > max_element:
                max_element = nums[i]
                index = i
                
        
        return index
        