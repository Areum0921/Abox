class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        answer = []
        nums = sorted(nums)
        for i in range(len(nums)-2):
            if i>0 and nums[i] == nums[i-1]:
                continue
            l,r = i+1,len(nums)-1
            while l<r:
                sum = nums[i] + nums[l] + nums[r]
                if sum>0: # 값이 양수면 r을 하나 줄여 더 작은 숫자로 이동
                    r -= 1
                elif sum<0: # 값이 음수면 l을 늘려 더 큰 숫자로 이동
                    l += 1
                else: # sum == 0
                    answer.append([nums[i],nums[l],nums[r]])
                    while l<r and nums[l]==nums[l+1]: # 같은 숫자일 경우 또 고려 안함
                        l += 1
                    while l<r and nums[r]==nums[r-1]:
                        r -= 1
                    l += 1
                    r -= 1
        return answer