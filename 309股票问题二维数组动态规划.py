
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
    def maxProfit(self, prices):
        # 方法1: 二维数组动态规划
        if not prices: return 0
        length = len(prices)
        dp = [[0 for i in range(3)] for i in range(length+1)]
        # 0 == have stock, dont' have to rest
        # 1 == don't have stock ,can buy
        # 2 == dont'have stock, cannot buy
        dp[0][0] = -prices[0]
        for i in range(1,length):
            dp[i][0] = max(dp[i-1][1]-prices[i], dp[i-1][0])
            ## state0 can be derive from: 
            ## 1. last state is 1, last state bought stock
            ## 2. last state is 0, don't do anything
            dp[i][1] = max(dp[i-1][2], dp[i-1][1])
            ## state1 can be derive from:
            ## 1. have to rest in the last day
            ## 2. don't have to rest in the last day
            dp[i][2] = dp[i][0]+prices[i]
            ## state2 can be derive from only: last timestep, sold stock
        return max(dp[length-1][1],dp[length-1][2])


             
        





def main():
    

    s = Solution()
    s.maxProfit([1,2,3,0,2])

    
    

main()










