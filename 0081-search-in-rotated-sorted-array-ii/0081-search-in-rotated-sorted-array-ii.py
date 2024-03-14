class Solution:

    def search(self, nums: List[int], target: int) -> bool:
        nums.sort()
        def binary_search(arr, low, high, x):
            if high >= low:
                mid = (high + low) // 2
                if arr[mid] == x:
                    return mid
                elif arr[mid] > x:
                    return binary_search(arr, low, mid - 1, x)
                else:
                    return binary_search(arr, mid + 1, high, x)
            else:
                return -1
            
        index = binary_search(nums, 0, len(nums)-1, target)
        if index ==-1:
            return False
        
        return True
        
        