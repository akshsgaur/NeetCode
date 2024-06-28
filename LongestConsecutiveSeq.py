class Solution:
    def longestConsecutive(self, nums):
        numSet = set(nums)
        longest = 0

        for n in nums:

            if (n-1) not in numSet:
                length = 0
                while (n + length) in numSet:
                    length += 1
                longest = max(length, longest)
        return longest

#Testing of the LongestConsecutive:

solution = Solution()
longest = solution.longestConsecutive([100,4,200,1,3,2])
print(longest)