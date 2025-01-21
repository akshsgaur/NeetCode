
'''
Longest Repeating Character Replacement
Solved 
You are given a string s consisting of only uppercase english characters and an integer k. You can choose up to k characters of the string and replace them with any other uppercase English character.

After performing at most k replacements, return the length of the longest substring which contains only one distinct character.

Example 1:

Input: s = "XYYX", k = 2

Output: 4
Explanation: Either replace the 'X's with 'Y's, or replace the 'Y's with 'X's.

Example 2:

Input: s = "AAABABB", k = 1

Output: 5

'''



class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        # Keeping the count of each character 
        count = {} 

        # Initializing the res number to return the final longest  
        # repeating character replacement
        res = 0
        # Initializing the left pointer 
        l = 0

        # Initializing and incrementing the right pointer to the end of the 
        # list 
        for r in range(len(s)):
            # Incrementing the count of the right most character encountered
            count[s[r]] = 1 + count.get(s[r], 0)
            # Having the equation LengthOfWindow - MaximumFrequencyOfLetters
            # in that window <= k, can potentially give us the most frequent characters,
            # So if the condition is not met, we move our left pointer and decrement the 
            # count of the characters 
            while (r-l+1) - max(count.values()) > k:
                count[s[l]] -= 1
                l += 1
            
            # Updating the result value if it encounters a new longest repeating character 
            # replacement
            res = max(res, r-l+1)
        
        #Returning result
        return res