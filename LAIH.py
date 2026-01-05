"""


You are given an array of integers heights where heights[i] represents the height of a bar. The width of each bar is 1.

Return the area of the largest rectangle that can be formed among the bars.

Note: This chart is known as a histogram.

Example 1:

Input: heights = [7,1,7,2,2,4]

Output: 8
Example 2:

Input: heights = [1,3,7]

Output: 7



"""


class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        
        # Calculate the max Area that needs to be returned, initially at 0
        maxArea = 0

        #The stack keeping track of the indexses and the heights that have come prior. 
        stack = [] #pair: [index, height]

        #Iterate thru indexes and heights in order to see which ones will need to be inserted or removed. 
        for i,h in enumerate(heights): 
            #the index that needs to be changed will start at the current index and then be manipulated to where the eventual start will be. 
            start = i

            #A while condition to see how many elements are actually in the stack that are greater than than the current value encountered. 
            while stack and h < stack[-1][1]: 
                # If a value is found where we have a value greater, pop it because we cannot continue it forward. 
                ind, hei = stack.pop()
                # See if the area that was calculated might be the max area calculated. 
                maxArea = max(maxArea, hei*(i-ind))
                #Change the start index to where it can be at the moment.  
                start = ind
            
            # append the new value to the stack. 
            stack.append([start, h])
            print("stack: ",stack)
        
        n= len(heights)
        for i,h in stack:
            maxArea =  max(maxArea, h * (n-i))
        

        return maxArea
