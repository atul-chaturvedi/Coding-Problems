class Solution:
    def minimizeMax(self, nums: List[int], p: int) -> int:
        nums.sort()
        left, right = 0, nums[-1] - nums[0]
        
        while left < right:
            mid = left + (right - left)//2
            count = 0
            i = 0
            while i < len(nums):
                # print(i)
                if(abs(nums[i-1] - nums[i]) <= mid):
                    count+=1
                    i+=1
                i = i+1
            
            # print()
            if count >= p:
                right = mid
            else:
                left = mid + 1
        
        # print()
        return left
            
        