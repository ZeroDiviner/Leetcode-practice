
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
    def restoreIpAddresses(self, s: str):
        self.res = []
        self.helper([],s);
        return list(set(map(lambda x:'.'.join(x), self.res)))

    def helper(self,arr,strLeft):
        if len(arr) == 4:
            if not strLeft:
                self.res.append(arr)
            else:
                return
        
        if strLeft[:1]:
             arr1=arr[:]
             arr1.append(strLeft[:1])
             self.helper(arr1,strLeft[1:])
        if strLeft[:2]:
             arr2=arr[:]
             arr2.append(strLeft[:2])
             self.helper(arr2,strLeft[2:])
        if strLeft[:3] and int(strLeft[:3])<=255:
            arr3=arr[:]
            arr3.append(strLeft[:3])
            self.helper(arr3,strLeft[3:])

          
        
        


             
        





def main():
    
    s = Solution()
    print(s.restoreIpAddresses("25525511135"))
    
    

main()










