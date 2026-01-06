"""

Koko Eating Bananas
Solved 
You are given an integer array piles where piles[i] is the number of bananas in the ith pile. You are also given an integer h, which represents the number of hours you have to eat all the bananas.

You may decide your bananas-per-hour eating rate of k. Each hour, you may choose a pile of bananas and eats k bananas from that pile. If the pile has less than k bananas, you may finish eating the pile but you can not eat from another pile in the same hour.

Return the minimum integer k such that you can eat all the bananas within h hours.

Example 1:

Input: piles = [1,4,3,2], h = 9

Output: 2
Explanation: With an eating rate of 2, you can eat the bananas in 6 hours. With an eating rate of 1, you would need 10 hours to eat all the bananas (which exceeds h=9), thus the minimum eating rate is 2.


"""

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        
        #Set the lower bound of binary search
        low = 1
        # set the upper bound of the binary search
        high = max(piles)
        k = high
        while low <= high: 
            mid = (low+high)//2
            k_i = mid
            sum_i = 0 
            for p in piles: 
                print(k_i)
                sum_i += math.ceil(float(p)/k_i)
            
            if sum_i <= h:
                k = k_i
                high = mid - 1
            else: 
                low = mid + 1
            
        return k
