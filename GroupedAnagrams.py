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

