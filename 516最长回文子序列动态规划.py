
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
     def longestPalindromeSubseq(self, s):
        n = len(s)
        dp = [ [0 if i!=j  else 1 for j in range(n)] for i in range(n)]
        for i in range(n-1,-1,-1):
            for j in range(i+1,n):
                if s[i] == s[j]:
                    dp[i][j] = dp[i+1][j-1] +2
                else:
                    dp[i][j] = max(dp[i][j-1], dp[i+1][j])
        return dp[0][n-1]
          
        
        


             
        





def main():
    
    s = Solution()
    s.longestPalindromeSubseq("bbbab")
    
    

main()










