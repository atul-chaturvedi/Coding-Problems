class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        ans =  []
# BRUTE FORCE APPROACH
#         mp = {}
#         for num in nums:
#             if num in mp:
#                 mp[num] +=1
#                 ans.append(num)
#             else:
#                 mp[num]  =1

# OPTIMAL SOLUTON
        for i in range(len(nums)):
            index = abs(nums[i]) -1
            
            # print(f"{i} {nums[i]} {index} {nums[index]}")
            
            if(nums[index] < 0):
                ans.append(index+1)
            else:
                nums[index] = nums[index] * -1
                
            
                
        return ans
            
            