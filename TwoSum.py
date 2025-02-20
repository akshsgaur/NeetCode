"""

Given an array of integers nums and an integer target, return the indices i and j such that nums[i] + nums[j] == target and i != j.

You may assume that every input has exactly one pair of indices i and j that satisfy the condition.

Return the answer with the smaller index first.

Example 1:

Input: 
nums = [3,4,5,6], target = 7

Output: [0,1]

"""

import time


class Solution():

    def mySolTwoSum(self, nums, target):
        length_of_nums = len(nums)
        for i in range(length_of_nums):
            for j in range(length_of_nums):
                if i == j:
                    continue
                else:
                    if nums[i] + nums[j] == target:
                        return [i,j]

    def recomTwoSum(self, nums, target):
        prevMap = {}
        for index, num in enumerate(nums):
            diff = target - num
            if diff in prevMap:
                return [prevMap[diff], index]
            prevMap[num] = index
        return


def main():
    solution = Solution()
    list_of_tests = [[[2,7,11,16],9], [[12,45,78,98,97],142]]
    for test in list_of_tests:
        start = time.time()
        myresult = solution.mySolTwoSum(test[0], test[1])
        end = time.time()
        total_time = end-start
        print("**** my code Statistics *****")
        print("Test: ", test)
        print("Result: ", myresult)
        print("Total Time: ", total_time)

        recommended_result = solution.recomTwoSum(test[0], test[1])
        end = time.time()
        total_time = end - start
        print("**** Recommended code Statistics *****")
        print("Test: ", test)
        print("Result: ", recommended_result)
        print("Total Time: ", total_time)


if __name__ == "__main__":
    main()

