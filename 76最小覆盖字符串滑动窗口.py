
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

from collections import defaultdict
class Solution:
     @wrapper
     def minWindow(self, s, t):
        if not t: return ''
        if not s: return False
        if len(s) < len(t): return ''
        need = defaultdict(int)
        window = defaultdict(int)
        for i in t:
            need[i]+=1
        left = right = 0
        match = 0
        res = None
        while right < len(s):
            c = s[right]
            if need.get(c):
                window[c]+=1
                if window[c] == need[c]:
                        match+=1
            right += 1
            while match == len(need):
                temp = s[left:right]
                if res == None:res = temp
                elif len(temp) < len(res): res = temp
                c_l = s[left]
                if window[c_l]: window[c_l] -=1
                if need.get(c_l) and  window[c_l] < need.get(c_l): match-=1
                left += 1
        return res if res != None else ''
          
        
        


             
        





def main():
    
    s = Solution()
    s.minWindow("ADOBECODEBANC","ABC")

    
    

main()










