class Solution:
    def findMin(self, nums: List[int]) -> int:
        # Edge case #
        if len(nums) == 0:
            return 0
        
        # Binary Search #
        res = nums[0]
        left = 0
        right = len(nums) - 1
        
        while left <= right:
            # If the left value is less than the right value, then we have sorted array and just return the minimum value without doing binary search #
            if nums[left] < nums[right]:
                res = min(nums[left], res)
                break
                
            mid = (left + right)//2
            res = min(res, nums[mid])
            
            # We are in the left sorted portion, we need to search right if mid value is greater than left and the min values will be on the right side because array is rotated #
            if nums[mid] >= nums[left]:
                left = mid + 1
            
            else:
                right = mid - 1
        return res

        