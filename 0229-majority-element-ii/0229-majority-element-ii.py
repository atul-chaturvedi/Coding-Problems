class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
#         n = len(nums)
#         count = dict()
#         for num in nums:
#             if num not in count:
#                 count[num] =1
#             else:
#                 count[num] +=1
#         ans = []
#         for c in count.keys():
#             if count[c] > n//3:
#                 ans.append(c)
                
#         return ans
        
        # This is how we have to aim for in python
        # list to map with frequency using Counter function
        # Counter(nums).items() to iterate keys and values
        # condtion v i,e value if greatet than len(nums)// 3
        # taking k i,e key when condition is true
        
        return [ k for k, v in Counter(nums).items() if v > len(nums) // 3 ]
            
        