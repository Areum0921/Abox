# 효율이 너무 안좋음 상위 5퍼, 8퍼
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:

        for i in nums:
            while nums.count(i) > 1:  # 해당 숫자가 1개될때까지 삭제
                nums.remove(i)

        return len(nums)  # 리스트가 아닌 개수 반환임

# 다른사람 코드 참고, 33%, 79%
# nums내 원소 재배치도 해야하며, 리턴값으로 중복되지 않는 숫자의 개수 리턴
# 바로 set해서 개수 리턴해도 nums가 일치하지 않기때문에 실패임.
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        i, idx = 0, 1
        while idx < len(nums):
            if nums[i] != nums[idx]:
                nums[i + 1] = nums[idx]
                i += 1
            idx += 1

        return i + 1