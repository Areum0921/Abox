"""
LeetCode : Two Sum
Runtime: 476 ms, faster than 5.07% of Python3 online submissions for Two Sum.
Memory Usage: 14.5 MB, less than 43.82% of Python3 online submissions for Two Sum.
"""

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        sorted_nums = sorted(nums)
        num1 = 0
        num2 = 0
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                if (nums[i] + nums[j] == target):
                    num1 = i
                    num2 = j
                    break

        return num1, num2