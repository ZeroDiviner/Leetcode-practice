
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
     def lengthOfLIS(self, nums):
        if not nums: return 0
        n = len(nums)
        dp = [1 for _ in range(n)]

        for i in range(1, n):
            for j in range(i):
                if nums[i] > nums[j]:
                    dp[i] = max(dp[i], dp[j]+1)
        return max(dp)
          
        
        


             
        





def main():
    
    s = Solution()
    s.lengthOfLIS([10,9,2,5,3,7,101,18])
    
    

main()










