from typing import *
class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        self.row = len(board)
        self.col = len(board[0])

        self.board = board
        self.word = word
        for i in range(self.row):
            for j in range(self.col):
                if self.dfs(i,j,board,0):
                    return True
        return False
    def dfs(self,si,sj,board, idx):
        if idx == len(self.word):
            return True
        if si < 0 or si >= self.row  or sj < 0 or sj >= self.col:
            return False
        if board[si][sj] == -1 or board[si][sj] != self.word[idx]:
            return False
        temp = board[si][sj]
        board[si][sj] = -1
        if self.dfs(si-1,sj,board, idx +1):
            return True
        if self.dfs(si+1,sj,board, idx +1):
            return True
        if self.dfs(si,sj-1,board, idx +1):
            return True
        if self.dfs(si,sj+1,board, idx +1):
            return True
        board[si][sj] = temp
        return False
board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]]
word = "ABCCED"
board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]]
word = "SEE"
board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]]
word = "ABCB"
board =[["A","B","C","E"],["S","F","E","S"],["A","D","E","E"]]
word = "ABCESEEEFS"
a = Solution()
print(*board,sep='\n')
print(a.exist(board,word))