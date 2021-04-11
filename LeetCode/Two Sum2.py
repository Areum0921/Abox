"""
LeetCode : Two Sum
Runtime: 76 ms, faster than 6.98% of Python3 online submissions for Two Sum.
Memory Usage: 14.5 MB, less than 10.95% of Python3 online submissions for Two Sum.
"""

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        num1 = 0
        num2 = 0
        for i in range(len(nums) - 1):
            # print(i)
            num1 = nums[i]  # 기준 숫자
            num2 = target - num1  # 찾아야 하는 숫자

            if (num2 in nums[i + 1:]):  # 찾아야할 숫자가 리스트에 있을때
                index1 = nums.index(num1)
                index2 = nums[i + 1:].index(num2) + index1 + 1  # index1 이후의 숫자들중에 num2의 인덱스 구하기.
                # print(index1,index2)
                break

        return index1, index2