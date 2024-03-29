import time

#Given an integer array nums, return true if any value appears at least twice in the array, and return false if every element is distinct.



#Example 1:

#Input: nums = [1,2,3,1]
#Output: true
#Example 2:

#Input: nums = [1,2,3,4]
#Output: false
#Example 3:

#Input: nums = [1,1,1,3,3,4,3,2,4,2]
#Output: true

#Adding Solution
class Solution:
    def myContainsDuplicate(self, nums) -> bool:
        list_of_visited = []
        for num in nums:
            if num not in list_of_visited:
                list_of_visited.append(num)
            else:
                return True
        return False

    def recomContainsDuplicate(self, nums) -> bool:
        hashset = set()
        for n in nums:
            if n in hashset:
                return True
            hashset.add(n)
        return False

def main():
    solution = Solution()
    list_of_tests = [[1,2,3,1], [1,2,3,4], [1,1,1,3,3,4,3,2,4,2]]
    for test in list_of_tests:
        start = time.time()
        myresult = solution.myContainsDuplicate(test)
        end = time.time()
        total_time = end-start
        print("**** my code Statistics *****")
        print("Test: ", test)
        print("Result: ", myresult)
        print("Total Time: ", total_time)

        recommended_result = solution.recomContainsDuplicate(test)
        end = time.time()
        total_time = end - start
        print("**** Recommended code Statistics *****")
        print("Test: ", test)
        print("Result: ", recommended_result)
        print("Total Time: ", total_time)


if __name__ == "__main__":
    main()