import re
class Solution:
    def compareVersion(self, v1: str, v2: str) -> int:
        v1 = [int(values) for values in v1.split(".") if len(values) > 0]
        v2 = [int(values) for values in v2.split(".") if len(values) > 0]
        
        # print(v1,v2)
        index = 0
        n1, n2 = len(v1), len(v2)
        for i in range(min(n1,n2)):
            # print(v1[i],v2[i])
            if v1[i] == v2[i]:
                index+=1
            elif int(v1[i]) > int(v2[i]):
                return 1
            else:
                return -1
            
            
            
        while(index < n1):
            if v1[index]==0:
                index+=1
            else:
                return 1
            
        while(index < n2):
            if v2[index]==0:
                index+=1
            else:
                return -1
                
            
            
            
        return 0 

        
            
        

        
        
    
            
        

            
        
        