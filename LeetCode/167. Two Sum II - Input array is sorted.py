class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l, r = 0, len(numbers) - 1

        while l < r:
            value = numbers[l] + numbers[r]
            if value == target:
                return [l + 1, r + 1]
            else:
                if value > target:
                    r -= 1
                elif value < target:
                    l += 1