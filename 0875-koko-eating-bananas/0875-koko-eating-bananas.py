import math
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        left = 1
        right = max(piles)
        ans = 10000000000
        
        while(left <= right):
            mid = (left+right)//2
            
     
            curr_time =0
            for pile in piles:
                curr_time += math.ceil(pile/mid)

            
            
            if curr_time > h:
                left = mid +1
            else:
                ans = min(ans, mid)
                right = mid-1
                
        return ans
            
