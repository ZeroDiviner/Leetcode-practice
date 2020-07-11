
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
from collections import Counter
from collections import defaultdict
class Solution:
     @wrapper
     def findAnagrams(self, s: str, p: str):
        if not s: return []
        need = Counter(p)
        window = defaultdict(int)
        match = 0
        left = right = 0
        length = len(s)
        res = []
        while right < length:
            char = s[right]
            if need.get(char): 
                window[char]+=1
                if window[char] == need.get(char):
                    match+=1
            right +=1
            while match == len(need):
                if len(s[left:right]) == len(p):
                    res.append(left)
                c_l = s[left]
                if need.get(c_l): 
                    window[c_l]-=1
                    if window[c_l]< need.get(c_l):match-=1
                    
                left +=1
        return res
          
        
        


             
        





def main():
    
    s = Solution()
    s.findAnagrams("cbaebabacd","abc")

    
    

main()










