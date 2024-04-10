class Solution:
    def timeRequiredToBuy(self, tickets: List[int], k: int) -> int:
        total_time = 0
        
        flag = True
        while flag:
            for i in range(len(tickets)):
                if tickets[k] ==0:
                    return total_time
                if tickets[i] > 0:
                    tickets[i] -=1
                    total_time +=1

            
        