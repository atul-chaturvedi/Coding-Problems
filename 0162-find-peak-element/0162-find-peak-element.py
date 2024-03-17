class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        # brute force approach
#         index = -1
#         max_element = -2147483649
        
#         for i in range(len(nums)):
#             if nums[i] > max_element:
#                 max_element = nums[i]
#                 index = i
                
        
#         return index

        #optimal approch using binary search
        low = 0
        high = len(nums) -1
        
        while(low <= high):
            mid = (low+high)//2
            
            if mid - 1 >= low and  nums[mid] < nums[mid -1]:
                high = mid -1
            elif mid +1 <= high and nums[mid] < nums[mid +1]:
                low = mid + 1
                
            else:
                return mid
        
        return -1
            
        