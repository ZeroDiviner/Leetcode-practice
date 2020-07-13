
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
        n = len(nums)
        res = []
        for i in range(n):
            num = nums[i]
            if res == []: res.append([num])
            else:
                left, right = 0, len(res)
                #[left,right)
                while left < right:
                    mid = left + (right-left)//2
                    if res[mid][-1] == num:
                        # left = mid+1
                        right = mid
                    elif res[mid][-1] > num:
                        right = mid
                    elif res[mid][-1] < num:
                        left = mid+1
                if left >= len(res): res.append([num])
                else: res[left].append(num)
                
        return len(res)
          
        
        


             
        





def main():
    
    s = Solution()
    s.lengthOfLIS([10,9,2,5,3,7,101,18])
    
    

main()










