
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
     def wrapper_function(self,*arc):
          start=time.time()
          res = func(self,*arc)
          end = time.time()
          print(f"Your function used {(end-start):.2f} seconds")
          print(f'Return value of your function is : \n{res}')
          return res
     return wrapper_function

class Solution:
     @wrapper
     def findMinArrowShots(self, points) -> int:
        points = sorted(points, key = lambda x:x[1])
        n = len(points)
        if n < 2: return n
        x = points[0]
        count = 0
        for i in range(1,n):
            end = x[1]
            if points[i][0] > end:
                x = points[i]
            else:
                count+=1
        return n-count
          
        
        


             
        





def main():
    
    s = Solution()
    s.findMinArrowShots([[10,16], [2,8], [1,6], [7,12]])
    
    

main()










