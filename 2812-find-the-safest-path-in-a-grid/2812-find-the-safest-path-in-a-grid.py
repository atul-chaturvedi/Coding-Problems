from queue import PriorityQueue
class Solution:
    def maximumSafenessFactor(self, grid: List[List[int]]) -> int:
        # we can use list as queue in python
        q = []
        directions = [1, 0, -1, 0, 1]
        n = len(grid)
        
        for i in range(0,n):
            for j in range(0, n):
                if grid[i][j] == 1:
                    q.append([i,j])
                    
                    
        
        while len(q) > 0:
            # we have to pass 0 index to pop first element
            curr = q.pop(0)
            
            i = curr[0]
            j = curr[1]
            
            for d in range(0, len(directions)-1):
                x = i + directions[d]
                y = j + directions[d+1]
                
                if(min(x,y) >=0 and max(x,y) <n and grid[x][y] == 0):
                    grid[x][y] = grid[i][j] +1
                    q.append([x,y])
                    

        
        # Python have Min Priority as default, and c++ have max priority as default
        pq =  PriorityQueue()
        
        # thats why we are making all the numbers negative, so most negative get highest priority
        # then we can use abs()  to make it positive
        pq.put([-grid[0][0], 0, 0])
        
        while True  :
            
            curr = pq.get()
            
            
            sf = curr[0]
            i = abs(curr[1])
            j = abs(curr[2])
            
            
            
            if(i >= n-1) and (j >= n-1):
                pq.put(curr)
                break
                

            for d in range(0, len(directions)-1):
                x = i+ directions[d]
                y = j + directions[d+1]
                
                if( min(x,y) >=0 and max(x,y) < n and grid[x][y] != -1):
                    pq.put([max(sf,-grid[x][y]), -x, -y])
                    grid[x][y] = -1
        
            
        return abs(pq.get()[0]) -1

        

        
    
