'''

Best Time to Buy and Sell Stock
Solved 
You are given an integer array prices where prices[i] is the price of NeetCoin on the ith day.

You may choose a single day to buy one NeetCoin and choose a different day in the future to sell it.

Return the maximum profit you can achieve. You may choose to not make any transactions, in which case the profit would be 0.

Example 1:

Input: prices = [10,1,5,6,7,1]

Output: 6
Explanation: Buy prices[1] and sell prices[4], profit = 7 - 1 = 6.

'''


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        if len(prices) == 1:
            return 0
        l,r=1,0
        maxReturn = 0 
        while(l<len(prices)):
            if prices[l] - prices[r] > 0:
                maxReturn = max(prices[l] - prices[r], maxReturn)
                l +=1
            else: 
                r = l
                l += 1

        return maxReturn