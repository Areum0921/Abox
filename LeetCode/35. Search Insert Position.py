# 43% 81%
# nums는 정렬되어있으므로 target보다 큰 숫자가 나왔다는건 target숫자가 없다는 뜻이다.
# 끝까지 돌았는데 target과 같거나, 큰 숫자를 못찾았으면 target이 nums의 제일 마지막값보다 큰 값.
class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:

        for i in range(len(nums)):
            if nums[i] >= target:
                return i

        return len(nums)

# 43% 94%
class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:

        if target > nums[-1]:
            return len(nums)
        if target < nums[0]:
            return 0

        for i in range(len(nums)):
            if nums[i] >= target:
                return i