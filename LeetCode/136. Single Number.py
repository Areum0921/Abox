class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        nums = sorted(nums) # 오름차순 정렬

        for i in range(len(nums) - 1):
            if i == 0: # 첫자리 숫자가 2번째자리 숫자랑 다르면 single
                if nums[i] != nums[i + 1]:
                    return nums[i]
            else: # 중간 숫자가 앞,뒤 숫자랑 다르면 single
                if nums[i - 1] != nums[i] and nums[i] != nums[i + 1]:
                    return nums[i]

        return nums[-1] # 앞과정을 통해 return 되지않았으면 맨 마지막 숫자가 single