
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
    def permute(self, nums):
        if not nums: return []
        self.res = []
        self.helper(nums, [])
        return self.res

    
    def helper(self, choice, path):
     ## 注意这一行的copy很重要，因为是回溯法，操作的都是同一数组的引用，如果不copy最后添加到res的都是空数组
     ## 可以取消注释下面一行试试
        if choice == []: self.res.append(path.copy())
        #if choice == []: self.res.append(path)
        for index, i in enumerate(choice):
            
            path.append(i)
            self.helper(choice[:index]+choice[index+1:], path)
            path.pop()



             
        





def main():
    s = Solution()
    s.permute([1,2,3])
    

main()










