class Solution:
    def arrangeCoins(self, n: int) -> int:
        step  = 0

        while n >= 0:
            n=n-(step+1)
            step+=1
            
            # print(step, n)
            
        return step-1
            
        