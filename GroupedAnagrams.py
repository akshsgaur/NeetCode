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

    def GroupedAnagrams(self, strs):
        res = defaultdict(list) #mapping charCount to the list of Anagrams

        for s in strs:
            count = [0] * 26

            for c in s:
                count[ord(c)-ord("a")] += 1

            res[tuple(count)].append(s)

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

