
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
     def lengthOfLongestSubstring(self, s: str) -> int:
        length = len(s)
        if length < 2:
            return length
        base = ''
        newlen = 0
        for i in range(length):
            if s[i] in base:
                base = base[base.index(s[i])+1:]
            base += s[i]
            l = len(base)
            if l > newlen:newlen = l
        return newlen
          
        
        


             
        





def main():
    
    s = Solution()
    s.lengthOfLongestSubstring("abcabcbb")

    
    

main()










