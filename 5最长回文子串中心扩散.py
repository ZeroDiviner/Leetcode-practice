
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
        def palindrome(s, i,j):
            while i >=0 and j < len(s) and s[i] == s[j]:
                i -= 1
                j += 1
            return s[i+1:j]
        res = ''
        for i in range(len(s)):
            r1 = palindrome(s, i, i)
            if len(r1) > len(res):
                res = r1
            r2 = palindrome(s, i, i+1)
            if len(r2) > len(res):
                res = r2
        return res
          
        
        


             
        





def main():
    
    s = Solution()
    s.longestPalindrome("babad")
    
    

main()










