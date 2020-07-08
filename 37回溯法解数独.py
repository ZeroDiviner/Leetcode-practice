
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
          print(f"Your function used {(end-start):.2f} seconds")
          print(f'Return value of your function is : \n{res}')
          return res
     return wrapper_function

class Solution:
    @wrapper
    def solveSudoku(self, board):
        """
        Do not return anything, modify board in-place instead.
        """
        self.rows = [set() for _ in range(9)]
        self.cols = [set() for _ in range(9)]
        self.box = [set() for _ in range(9)]
        self.base = set(str(i) for i in range(1, 10))
        self.count = 0
        self.empty = []
        for row in range(9):
            for col in range(9):
                ele = board[row][col]
                if ele!='.':
                    self.rows[row].add(ele)
                    self.cols[col].add(ele)
                    self.box[(row//3)*3 + col//3].add(ele)
                    self.count +=1
                else:
                    self.empty.append((row,col))
        self.helper(board, 0)
        print(board)

    def helper(self, board, index):
        if index == len(self.empty): return True

        i = self.empty[index]
        row, col = i[0], i[1]
        choice = self.base - self.rows[row] - self.cols[col] - self.box[(row//3)*3 + col//3]
        for c in choice:
             board[row][col] = c
             self.rows[row].add(c)
             self.cols[col].add(c)
             self.box[(row//3)*3 + col//3].add(c)
             
             if self.helper(board, index+1): return True
             board[row][col] = '.'
             self.rows[row].remove(c)
             self.cols[col].remove(c)
             self.box[(row//3)*3 + col//3].remove(c)


             
        





def main():
    li = [["5","3",".",".","7",".",".",".","."],["6",".",".","1","9","5",".",".","."],[".","9","8",".",".",".",".","6","."],["8",".",".",".","6",".",".",".","3"],["4",".",".","8",".","3",".",".","1"],["7",".",".",".","2",".",".",".","6"],[".","6",".",".",".",".","2","8","."],[".",".",".","4","1","9",".",".","5"],[".",".",".",".","8",".",".","7","9"]]

    s = Solution()
    s.solveSudoku(li)
    

main()










