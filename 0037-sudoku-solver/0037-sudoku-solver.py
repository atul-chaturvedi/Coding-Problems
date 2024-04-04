class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        def is_ok(board, row, col, num):
            for i in range(0, 9):
                if board[row][i] == str(num):
                    return False
                elif board[i][col] == str(num):
                    return False
                
            row_box = row - row%3
            col_box = col - col%3
            
            for i in range(row_box, row_box+3):
                for j in range(col_box, col_box+3):
                    if board[i][j] == str(num):
                        return False
            
            return True
            
                    
        def dfs(row, col):
            if row >= len(board[0]) :
                return True 
            
            if col >= len(board[0]):
                return dfs(row+1,0)
                
            if board[row][col] !='.':
                return dfs(row,col+1)
            
            for num in range(1, 10):
                if(is_ok(board, row, col, num)):
                    board[row][col] = str(num)
                    if dfs(row, col+1):
                        return True
                    else:
                        board[row][col] = '.'
                        
                        
            return False
            
            
        
        for i  in range(0, 9):
            for j in range(0, 9):
                if board[i][j] == '.':
                    dfs(i,j)
            
            
            
            
        