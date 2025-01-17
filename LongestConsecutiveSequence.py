
'''

Longest Consecutive Sequence
Solved 
Given an array of integers nums, return the length of the longest consecutive sequence of elements that can be formed.

A consecutive sequence is a sequence of elements in which each element is exactly 1 greater than the previous element. The elements do not have to be consecutive in the original array.

You must write an algorithm that runs in O(n) time.

Example 1:

Input: nums = [2,20,4,10,3,4,5]

Output: 4
Explanation: The longest consecutive sequence is [2, 3, 4, 5].

Example 2:

Input: nums = [0,3,2,5,4,6,1,1]

Output: 7

'''



class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # Creating a numSet that stores all the values nums
        numSet = set(nums)
        # Tracker of the longest value
        longest = 0

        #Going through each element in nums   
        for n in nums: 
            #A condition to check if n is a start of a sequence, if it is 
            #not, it may be a start of a sequence. 
            if (n-1) not in numSet: 
                # Initializing a length to keep track of the length of the list
                length = 0
                #If n + length is in the numSet, increment the length
                while (n+length) in numSet: 
                    length += 1
                #Onec reached the end of a sequence, update the longest value
                longest = max(length, longest)
        #Return longest
        return longest