
import time
##class TreeNode:
##     def __init__(self, x):
##         self.val = x
##         self.left = None
##         self.right = None

##class ListNode:
##     def __init__(self, x):
##          self.val = x
##          self.next = None

##class RandomListNode:
##     def __init__(self, x):
##          self.label = x
##          self.next = None
##          self.random = None
from functools import wraps
def wrapper(func):
     
     @wraps(func)
     def wrapper_function(self,arc):
          start=time.time()
          res = func(self,arc)
          end = time.time()
          print(f"Your function used {(end-start)*1000:.2f} seconds")
          print(f'Return value of your function is : \n{res}')
          return res
     return wrapper_function

from collections import defaultdict
class Solution:
    @wrapper
    def isValidSudoku(self, board):
        if board ==[[]]: return True
        n = len(board)
        rows = [defaultdict(int) for _ in range(n)]
        cols = [defaultdict(int) for _ in range(n)]
        box = [defaultdict(int) for _ in range(n)]
        for i in range(n):
            for j in range(n):
                if board[i][j] != '.':
                    ele = int(board[i][j])
                    if rows[i][ele]: return False
                    if cols[j][ele]: return False
                    if box[(i//3)*3 + j//3][ele]:return False
                    rows[i][ele] = 1
                    cols[j][ele] = 1
                    box[(i//3)*3 + j//3][ele] = 1
        return True


##    def check(self, matrix, row, col):
##        length = len(matrix)
##        c1, c2 = col - 1, col+1
##        for i in range(row):
##            if matrix[i][col] == 'Q':
##                return False
##        r,c = row-1, col-1
##        while r >=0 and c >=0:
##            if matrix[r][c] == 'Q': return False
##            r-=1
##            c-=1
##        r,c = row-1, col+1
##        while r >=0 and c <len(matrix):
##            if matrix[r][c] == 'Q': return False
##            r-=1
##            c+=1
##        return True



             
        





def main():
    li = [ ["5","3",".",".","7",".",".",".","."],
           ["6",".",".","1","9","5",".",".","."],
           [".","9","8",".",".",".",".","6","."],
           ["8",".",".",".","6",".",".",".","3"],
           ["4",".",".","8",".","3",".",".","1"],
           ["7",".",".",".","2",".",".",".","6"],
           [".","6",".",".",".",".","2","8","."],
           [".",".",".","4","1","9",".",".","5"],
           [".",".",".",".","8",".",".","7","9"]
          ]

    s = Solution()
    s.isValidSudoku(li)
    

main()










