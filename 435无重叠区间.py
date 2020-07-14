
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
     def eraseOverlapIntervals(self, intervals) -> int:
        intervals = sorted(intervals, key = lambda x: x[1] )
        n = len(intervals)
        if n < 2: return 0
        x = intervals[0]
        count = 0
        for i in range(1,n):
            end = x[1]
            if intervals[i][0] >= end:
                x = intervals[i]
            else:
                count+=1
        return count 
          
        
        


             
        





def main():
    
    s = Solution()
    s.eraseOverlapIntervals([ [1,2], [1,2], [1,2] ])
    
    

main()










