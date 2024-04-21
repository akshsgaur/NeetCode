import time
# Given two strings s and t, return true if t is an anagram of s, and false otherwise.
#
# An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.

class Solution:

        def remove_duplicates(self, s: str):
            list_of_separates = []
            for letter in s:
                if letter not in list_of_separates:
                    list_of_separates.append(letter)

            return list_of_separates

        def myisAnagram(self, s: str, t: str) -> bool:
            if len(s) != len(t):
                return False
            separates = self.remove_duplicates(s)
            print("separates: ", separates)
            for letter in separates:
                if s.count(letter) != t.count(letter):
                    return False
            return True

        def recomisAnagram(self, s:str, t:str) -> bool:
            if len(s) != len(t):
                return False
            countS, countT = {}, {}
            for i in range(len(s)):
                countS[s[i]] = 1+countS.get(s[i],0)
                countT[t[i]] = 1+countT.get(t[i],0)
            for c in countS:
                if countS[c] != countT.get(c,0):
                    return False
            return True

def main():
    solution = Solution()
    list_of_tests =[["anagram","nagaram"], ["rat","car"]]
    for test in list_of_tests:
        start = time.time()
        myresult = solution.myisAnagram(test[0], test[1])
        end = time.time()
        total_time = end-start
        print("**** my code Statistics *****")
        print("Test: ", test)
        print("Result: ", myresult)
        print("Total Time: ", total_time)

        recommended_result = solution.recomisAnagram(test[0], test[1])
        end = time.time()
        total_time = end - start
        print("**** Recommended code Statistics *****")
        print("Test: ", test)
        print("Result: ", recommended_result)
        print("Total Time: ", total_time)


if __name__ == "__main__":
    main()

