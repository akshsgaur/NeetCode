'''

Top K Frequent Elements
Solved 
Given an integer array nums and an integer k, return the k most frequent elements within the array.

The test cases are generated such that the answer is always unique.

You may return the output in any order.

Example 1:

Input: nums = [1,2,2,3,3,3], k = 2

Output: [2,3]
Example 2:

Input: nums = [7,7], k = 1

Output: [7]

Time Complexity <- O(n)
Space Complexity <- O(n)

Neetcode link: https://neetcode.io/problems/top-k-elements-in-list

'''

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        #Creating a count hashmap to store the count of each number for example, 
        # if 1 occurs 3 time, it will be 1:3
        count = {}
        #a list to store the counts in each index, for example, if 1 and 2 occurs 3 times, freq[2] = [1,2]
        freq = [[] for i in range(len(nums)+1)]

        # Running a for loop that will store how many times a certain number will occur, for example, if 1 occurs three times, 
        # count[1] = 3
        for n in nums:
            count[n] = 1 + count.get(n,0)
        print(count)
        #Going through each count and appending that to that index
        for n,c in count.items():
            freq[c].append(n)
        
        print(freq)
        #initializing the result list
        res = []
        #Going backwards in the list to get the most frequent
        for i in range(len(freq)-1, 0, -1):
            # going through all the elements in particular index
            for n in freq[i]: 
                res.append(n)
                if len(res) == k:
                    return res