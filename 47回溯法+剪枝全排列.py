
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
     def wrapper_function(self,arc):
          start=time.time()
          res = func(self,arc)
          end = time.time()
          print(f"Your function used {(end-start)*1000:.2f} seconds")
          print(f'Return value of your function is : \n{res}')
          return res
     return wrapper_function


class Solution:
    @wrapper
    def permuteUnique(self, nums):
        nums.sort()
        self.res = []
        self.helper(nums, [])
        return self.res

    def helper(self, choice, path):
        if not choice: self.res.append(path[:])
        for i in range(len(choice)):
            if i-1>=0 and choice[i] == choice[i-1]: continue
            self.helper(choice[:i]+choice[i+1:], path+[choice[i]])



             
        





def main():
    s = Solution()
    s.permuteUnique([1,1,2])
    

main()










