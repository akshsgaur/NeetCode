
'''

Longest Substring Without Repeating Characters
Solved 
Given a string s, find the length of the longest substring without duplicate characters.

A substring is a contiguous sequence of characters within a string.

Example 1:

Input: s = "zxyzxyz"

Output: 3
Explanation: The string "xyz" is the longest without duplicate characters.

Example 2:

Input: s = "xxxx"

Output: 1

'''


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # Creating the charset that is added to removed based
        # the characters encountered 
        charSet = set()
        # initializing the left point
        l = 0
        # initializing the res variable 
        res = 0 
        # initializing the right point to go till the end of the 
        # list and maniputing charSet as we encounter repeated string
        for r in range(len(s)):
            #Moving the pointer until a duplicate character is reached
            while s[r] in charSet:
                # once a duplicating character is encountered, we remove
                # the left most character because the string is contigous
                charSet.remove(s[l])
                # we also move the left pointer by one
                l += 1
            
            # Once we have moved and removed the corresponding character 
            # according to their duplicacy, we then add the right most character
            # to continue iterating the string
            charSet.add(s[r])
            # we may have potentially found the longest substring without repeating 
            # character, so we update the result 
            res = max(res, r-l+1)
        
        # we return the result. 
        return res
