class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        board = [['.' for _ in range(n)] for _ in range(n)]
        ans = []
        # print(board)
        def check(board, row, col):
            #horizontally and vertically
            for i in range(0, n):
                if board[row][i] =='Q':
                    return False
                elif board[i][col] =='Q':
                    return False
            # diagonally
                elif row+i < n and col+i <n and board[row+i][col+i] =='Q':
                    return False
                elif row-i >=0 and col-i >=0 and board[row-i][col-i] =='Q':
                    return False
                elif row+i < n and col-i >=0 and board[row+i][col-i] =='Q':
                    return False
                elif row-i >=0 and col+i < n and board[row-i][col+i] == 'Q':
                    return False
                
            return True
            
        
        def dfs(board, row):
            if row==n:
                ans.append(["".join(row) for row in board])
                return
            
            if row > n :
                return
            
            for col in range(0, n):
                if check(board, row, col):
                    board[row][col] ='Q'
                    dfs(board, row+1)
                    board[row][col] = '.'
            
            
        dfs(board, 0)
        return ans
            