class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        n = len(nums)
        count = dict()
        for num in nums:
            if num not in count:
                count[num] =1
            else:
                count[num] +=1
        ans = []
        for c in count.keys():
            if count[c] > n//3:
                ans.append(c)
                
        return ans
            
        