'''

Container With Most Water
Solved 
You are given an integer array heights where heights[i] represents the height of the ith

You may choose any two bars to form a container. Return the maximum amount of water a container can store.

Example 1:

Input: height = [1,7,2,5,4,7,3,6]

Output: 36
Example 2:

Input: height = [2,2,2]

Output: 4


'''


class Solution:
    def maxArea(self, heights: List[int]) -> int:
        #Setting the initial value of maxArea to 0
        maxArea = 0
        #Initializing the left and the right pointer
        l,r = 0, len(heights) - 1

        #Running the while loop for two pointers
        while l < r:
            # Computing the area of the rectangle
            Area = (r-l) * min(heights[l], heights[r])
            # Changing the area to be the max of the area computed 
            # and the previous maxArea
            maxArea = max(maxArea, Area)
            # If the height of left is more than height of right, 
            # we have to reduce the right pointer to one less
            if heights[l] >= heights[r]:
                r -= 1
            # If the height of right is more than height of left, 
            # we have to increase the left pointer to one more
            else: 
                l += 1
        
        #Return the maxArea
        return maxArea