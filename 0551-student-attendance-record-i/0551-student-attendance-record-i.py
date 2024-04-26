class Solution:
    def checkRecord(self, s: str) -> bool:
        count_A =0
        late_flag = False
        for i in range(len(s)):
            if s[i] == 'A':
                count_A +=1
                
            if i+2 < len(s) and s[i+2]=='L' and s[i+1] =='L' and s[i] =='L':
                late_flag = True
                
        
        if count_A < 2 and not late_flag:
            return True
        
        return False

                
                
        
        