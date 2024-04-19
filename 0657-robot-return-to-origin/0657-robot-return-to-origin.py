class Solution:
    def judgeCircle(self, moves: str) -> bool:
        x,y = 0,0
        for move in moves:
            if move == 'U':
                y = y+1
            elif move =='D':
                y = y-1
            elif move == 'L':
                x = x+1
            else:
                x = x-1
                
                
        
        if x == 0 and y== 0:
            return True
        
        return False
        