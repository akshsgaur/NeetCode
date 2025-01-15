"""

Encode and Decode Strings
Solved 
Design an algorithm to encode a list of strings to a single string. The encoded string is then decoded back to the original list of strings.

Please implement encode and decode

Example 1:

Input: ["neet","code","love","you"]

Output:["neet","code","love","you"]
Example 2:

Input: ["we","say",":","yes"]

Output: ["we","say",":","yes"]



"""

class Solution:

    def encode(self, strs: List[str]) -> str:
        #The final encoded string that needs to be returned 
        res = "" 
        #Going through each element of the list 
        for s in strs: 
            #strong it in the res list as "Length of the string" + "#" + "The word itself"
            # For example if the word is: ["neet", "code"] it will be saved as: "4#neet4#code"
            res += str(len(s)) + "#" + s 
        
        #Returning the result
        return res


    def decode(self, s: str) -> List[str]:

        # Initializing the result list and an index that will store the list of the result and the index tracker
        # for the string
        res, i = [],0
        # Running a while loop until the length of the encoded string
        while i < len(s): 
            # Having a sub index to track the indexes of the word with it so for example if the string "4#neet" <- j will keep track of 4 # and neet 
            
            #initializing the j index to where i is at that particular point
            j = i
            # Moving the j iterative to the letter "#"
            while s[j] != "#":
                j += 1

            #Getting length of the string, for example, if the string is "4#neet", length will go from 0->1
            length = int(s[i:j])
            #This will give us the string 
            sr = s[j+1:j+1+length]
            #We will append this to the result string
            res.append(sr)
            #Updating the value of i for the next iteration
            i = j + 1 + length
        
        #Returning the result
        return res