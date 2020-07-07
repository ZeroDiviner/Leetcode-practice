
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

from copy import deepcopy
class Solution:
    @wrapper
    def solveNQueens(self, n):
        if not n: return []
        if n == 1: return [Q]
        matrix = [ ['.' for i in range(n)] for _ in range(n)]
        self.res = []
        self.queen(matrix, 0)
        return self.res
    
    def queen(self, matrix, rownum):
        n = len(matrix)
        if rownum == n:
            #print(matrix)
            #self.res.append(deepcopy(matrix))
            ## 注意这里曾经碰到问题，当直接 self.res.append(matrix) 的时候因为 matrix 是个
            ##  二维数组，所以即使 matrix[::]也不会新建对象，所以在回溯法中还是会被下面的
            ## matrix[rownum][i] = '.'改成 全为'.'的数组，所以如果要保留二维数组需要 deepcopy
            self.res.append(list(map(lambda x: ''.join(x), matrix)))
            return 
        for i in range(n):
            
            if not self.check(matrix, rownum, i):continue
                 
            matrix[rownum][i] = 'Q' 
            #print(matrix)
            self.queen(matrix, rownum+1)
            matrix[rownum][i] = '.'
     ##  三个循环合成一个循环，速度居然比三个循环慢？
    def check(self, matrix, row, col):
        length = len(matrix)
        c1, c2 = col - 1, col+1
        for i in range(row-1, -1, -1):
            if matrix[i][col] == 'Q':
                return False
            if c1 >=0 and matrix[i][c1] == 'Q': return False
            if c2 <length and matrix[i][c2] == 'Q': return False
            c1-=1
            c2+=1
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
    s = Solution()
    s.solveNQueens(4)
    

main()










