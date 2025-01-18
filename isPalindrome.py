'''

Valid Palindrome
Solved 
Given a string s, return true if it is a palindrome, otherwise return false.

A palindrome is a string that reads the same forward and backward. It is also case-insensitive and ignores all non-alphanumeric characters.

Example 1:

Input: s = "Was it a car or a cat I saw?"

Output: true
Explanation: After considering only alphanumerical characters we have "wasitacaroracatisaw", which is a palindrome.

Example 2:

Input: s = "tab a cat"

Output: false
Explanation: "tabacat" is not a palindrome.

'''



class Solution:
    def isPalindrome(self, s: str) -> bool:
        # Setting the left and right pointer 
        l,r = 0, len(s) - 1
        # Running the pointers only until l is less than r to avoid
        # overlapping
        while l < r: 
            
            # Looking to see if the character at l is a alphanumeric, 
            # if it is not alphanumeric, move the left pointer by 1 until 
            # it meets a alphanumeric value, and since we donot want the l pointer 
            # to go over bounds while traversing, we have l < r
            while l < r and not self.alphaNum(s[l]):
                l += 1
            
            # The same thing as before, but in this case we are decrementing the value of r by 1
            # and seeing it doesn't go out of bounds. 
            while r > l and not self.alphaNum(s[r]):
                r -= 1

            # Once we know that we are in the right positions from both the sides, 
            # We are going to be checking if they equal or not, if not, we will return 
            # False because they are not palindromes
            if s[l].lower() != s[r].lower():
                return False
            # Updating the pointers to accomodate the next characters 
            l, r = l+1, r-1
        
        # If the loop runs completely, we know it's a palindrome and we return 
        # True
        return True

    
    # An alphanumeric function to see if a character is a Alphanumeric 
    # value or not and we do that by looking at the ord values of the character, 
    # if it in between "A" and "Z", "a" and "z" or "0" and "9", we can say it's 
    # a alphanumeric value. 
    def alphaNum(self, c):

        return (ord("A") <= ord(c) <= ord("Z") or 
                ord("a") <= ord(c) <= ord("z") or
                ord("0") <= ord(c) <= ord("9") )