
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
     def longestPalindrome(self, s):
        if not s: return ""
        n = len(s)
        dp = [[ 0 for _ in range(n)] for i in range(n) ]
        for i in range(n):
            dp[i][i] = 1
        res = s[0]
        for i in range(n-1,-1,-1):
            for j in range(i+1, n):
                if j-i<2 and s[i] == s[j]: 
                    dp[i][j] = 1
                    res = s[i:j+1] if len(s[i:j+1])>len(res) else res
                else:
                    if i+1<n and j-1 >=0 and dp[i+1][j-1]==1 and s[i] == s[j]:
                        dp[i][j] = 1
                        res = s[i:j+1] if len(s[i:j+1])>len(res) else res
        return res
          
        
        


             
        





def main():
    
    s = Solution()
    s.longestPalindrome("babad")
    
    

main()










