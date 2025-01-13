'''
Group Anagrams
Given an array of strings strs, group all anagrams together into sublists. You may return the output in any order.

An anagram is a string that contains the exact same characters as another string, but the order of the characters can be different.

Example 1:

Input: strs = ["act","pots","tops","cat","stop","hat"]

Output: [["hat"],["act", "cat"],["stop", "pots", "tops"]]
Example 2:

Input: strs = ["x"]

Output: [["x"]]
Example 3:

Input: strs = [""]

Output: [[""]]

'''





from collections import defaultdict
import time

class Solution:

    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # The res that we will store the key and the value in
        # and then return the values of the list in
        res = defaultdict(list)

        #Looping through each string
        for s in strs: 
            # Creating a list of 26 characters which we will manipulate each value in the 
            # list
            count = [0] * 26
            
            #Going through each character in the string and then manipulating the 
            #index to add 1 to that list
            for c in s: 
                # ord(c) - ord("a") will give us the index of that character, for
                # example c will be 2 - 0 
                count[ord(c) - ord("a")] += 1

            #creating a key of the list count, while the value will be that string
            res[tuple(count)].append(s)

        #Returning the value
        return res.values()


def main():
    solution = Solution()
    list_of_tests = ["eat","tea","tan","ate","nat","bat"]
    for test in list_of_tests:
        start = time.time()
        result = solution.GroupedAnagrams(list_of_tests)
        end = time.time()
        total_time = end - start
        print("**** my code Statistics *****")
        print("Test: ", test)
        print("Result: ", result)
        print("Total Time: ", total_time)



if __name__ == "__main__":
    main()

