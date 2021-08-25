# 47%, 60%
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        answer = nums[0]

        for i in range(1, len(nums)):
            nums[i] = max(nums[i], nums[i - 1] + nums[i])
            answer = max(answer, nums[i])

        return answer