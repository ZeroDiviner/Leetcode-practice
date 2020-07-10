
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
        ## 方法二： 有限状态机
        if not prices: return 0
        ## Finite state maching
        ## 在某个时间t，一定有 3 种states：
        ## 1. have状态，上一状态可能是have，或者canbuy
        ## 2. canbuy状态，上一状态可能是canbuy然后这一时间不变，或者上一时间cant_buy，这一时间是可以买的
        ## 3. cant_buy状态，上一状态只可能是have，然后这一时间卖掉了
        length = len(prices)
        have = -prices[0]
        cant_buy = -float('Inf')
        can_buy = 0
        # cant_buy = 0
        for i in range(1, length):
            have_ = have
            c = can_buy
            have = max(c - prices[i], have_)
            can_buy = max(c, cant_buy)
            cant_buy = have_+prices[i]
        return max(can_buy, cant_buy)


             
        





def main():
    

    s = Solution()
    s.maxProfit([1,2,3,0,2])

    
    

main()










