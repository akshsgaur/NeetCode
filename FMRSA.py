'''

Find Minimum in Rotated Sorted Array
Solved 
You are given an array of length n which was originally sorted in ascending order. It has now been rotated between 1 and n times. For example, the array nums = [1,2,3,4,5,6] might become:

[3,4,5,6,1,2] if it was rotated 4 times.
[1,2,3,4,5,6] if it was rotated 6 times.
Notice that rotating the array 4 times moves the last four elements of the array to the beginning. Rotating the array 6 times produces the original array.

Assuming all elements in the rotated sorted array nums are unique, return the minimum element of this array.

A solution that runs in O(n) time is trivial, can you write an algorithm that runs in O(log n) time?

Example 1:

Input: nums = [3,4,5,6,1,2]

Output: 1
Example 2:

Input: nums = [4,5,0,1,2,3]

Output: 0

'''

class Solution:
    def findMin(self, nums: List[int]) -> int:
        #Initializing res to be equal to nums[0], 
        #randomly, it may or may not be the right answer
        res = nums[0]
        # Setting the right and the left pointer
        l,r=0,len(nums)-1
        #While condition loop 
        while l<=r:
            # If the left of the list is more than the right 
            # of the list, it is safe to say that will be the 
            # least of the list, so we can try to assign 
            #the min to left of the list
    
            if nums[l] < nums[r]:
                res = min(res, nums[l])
                break

            # If the left of the list is not less than the right of the list
            # then we will look at the middle of the list and perform a binary 
            # search
            m = (l+r)//2
            # setting the min value to the middle of the list and then 
            # iterating through the right according the values on the right and 
            # the left of the list
            res = min(res, nums[m])
            if nums[m] >= nums[l]:
                l = m+1 
            else: 
                r = m-1
        #Returning the res
        return res