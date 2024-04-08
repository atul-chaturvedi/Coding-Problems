class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        
        def dfs(borad,r, c, word_index):
            if word_index >= len(word):
                return True
            
            if r < 0 or c < 0 or  r >= len(board) or c >= len(board[0]) or board[r][c] =="#" or board[r][c] != word[word_index]:
                return False
            
            curr_char = word[word_index]                 
            board[r][c] = "#"
                             
            # print(f"r:{r}, c:{c}, word_index:{word_index}, curr_char:{board[r][c]}")
            
            bottom = dfs(board[:], r+1, c, word_index+1)
            top = dfs(board[:], r-1, c, word_index+1)
            right = dfs(board[:], r, c+1, word_index+1)
            left = dfs(board[:], r, c-1, word_index+1)
            
            
            
            board[r][c] = curr_char
            # word_index -=1
            
            return left or right or bottom or top
            
        
        for i in range(len(board)):
            for j in range(len(board[0])):
                if dfs(board[:], i,j,0):
                    return True
        
        return False
        
            
        