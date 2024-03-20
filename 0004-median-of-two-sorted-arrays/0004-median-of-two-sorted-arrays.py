import math
class Solution:
    
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        #Brute Force Approach
        def sorted_join(nums1, nums2):
            n1 = len(nums1)
            n2 = len(nums2)
            nums = []
            i = 0
            j = 0
            
            while i < n1 and j < n2:
                if nums1[i] < nums2[j]:
                    nums.append(nums1[i])
                    i=i+1
                else:
                    nums.append(nums2[j])
                    j=j+1
                    
            
            while i < n1:
                nums.append(nums1[i])
                i+=1
            
            while j < n2:
                nums.append(nums2[j])
                j+=1
            
            return nums
            
        nums = sorted_join(nums1, nums2)
        n = len(nums1) + len(nums2)
        
        if n%2 == 1:
            return nums[n//2]
        else:
            return (nums[(n-1)//2] + nums[(n)//2])/2