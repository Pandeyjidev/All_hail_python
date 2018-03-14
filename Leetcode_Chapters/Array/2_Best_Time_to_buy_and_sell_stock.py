# https://leetcode.com/explore/interview/card/top-interview-questions-easy/92/array/564/
# Say you have an array for which the ith element is the price of a given stock on day i.

# Design an algorithm to find the maximum profit. You may complete as many transactions 
# as you like (ie, buy one and sell one share of the stock multiple times). 
# However, you may not engage in multiple transactions at the same time 
# (ie, you must sell the stock before you buy again).

class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        l = len(prices)
        if l < 2:
            return 0
        diff = [prices[i]-prices[i-1] for i in range(1,l)]
        res = [i for i in diff if i>0]
        return sum(res)
    