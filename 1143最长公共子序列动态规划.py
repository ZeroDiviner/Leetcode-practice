
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
     def longestCommonSubsequence(self, text1, text2):
        n = len(text1)
        m = len(text2)
        dp = [ [0 for _ in range(n+1)] for i in range(m+1)]
        for i in range(1,m+1):
            for j in range(1,n+1):
                if text2[i-1] == text1[j-1]:
                    dp[i][j] = dp[i-1][j-1]+1
                else:
                    dp[i][j] = max(dp[i-1][j], dp[i][j-1])
        return dp[m][n]
          
        
        


             
        





def main():
    
    s = Solution()
    s.longestCommonSubsequence("abcde","ace")
    
    

main()










