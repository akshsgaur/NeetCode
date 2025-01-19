'''

3Sum
Solved 
Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] where nums[i] + nums[j] + nums[k] == 0, and the indices i, j and k are all distinct.

The output should not contain any duplicate triplets. You may return the output and the triplets in any order.

Example 1:

Input: nums = [-1,0,1,2,-1,-4]

Output: [[-1,-1,2],[-1,0,1]]
Explanation:
nums[0] + nums[1] + nums[2] = (-1) + 0 + 1 = 0.
nums[1] + nums[2] + nums[4] = 0 + 1 + (-1) = 0.
nums[0] + nums[3] + nums[4] = (-1) + 2 + (-1) = 0.
The distinct triplets are [-1,0,1] and [-1,-1,2].




'''




class Solution:
    
    def threeSum(self, nums):

        res = []
        nums.sort

        for i, a in enumerate(nums):

            if i > 0 and a == nums[i-1]:
                continue

            l,r = i + 1, len(nums) - 1
            while l < r: 
                threeSum = a + nums[l] + nums[r]
                if threeSum > 0:
                    r -= 1
                elif threeSum < 0:
                    l += 1
                else: 
                    res.append([a, nums[l], nums[r]])
                    l+=1
                    while nums[l] == nums[l-1] and l < r:
                        l += 1
        
        return res

    
    
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        #Initializing the result list
        res = []
        #Sorting the list to not consider duplicate numbers 
        nums.sort()

        # Going through numbers and their indexes
        for i,a in enumerate(nums):

            # If the index is greater than 0 and a is not the same 
            # value as previous value, continue, which is why we sorted
            if i > 0 and nums[i-1] == a:
                continue 
            #Initializing the left and right pointer
            l, r = i + 1, len(nums) - 1

            #Going through the 2 sum approach
            while l<r:
                # If the threeSum is greater than 0, that means 
                # we have to reduce the right point 
                if a + nums[l] + nums[r] > 0:
                    r -= 1
                # If the threeSum is less than 0, that means we have 
                # increase the left point, all of this possible because
                # the list is sorted
                elif a + nums[l] + nums[r] < 0:
                    l += 1
                else: 
                    # this means the Threesome is 0, we need 
                    # to append the values to the result
                    res.append([a, nums[l], nums[r]])
                    l += 1
                    # r -= 1
                    # Increasing the left pointer to the value in which 
                    # it is not equal to the previous value [l-1] != [l]
                    while nums[l] == nums[l-1] and l < r:
                        l += 1
        
        #Returning the res
        return res