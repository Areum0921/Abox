# 36ms, 77%
class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        i = 0
        lenght = len(nums)
        cnt = 0 # 중복된 숫자 개수
        while i < lenght:
            if nums[i - cnt] == val:
                nums.remove(nums[i - cnt]) # 지우면 인덱스가 줄어듦
                cnt += 1
            i += 1

        return lenght - cnt # 남은 숫자 개수

# 속도는 같은데 위에가 메모리 효율 더좋음. 16%
class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        i = 0
        for j in range(len(nums)):
            if nums[j] != val:
                nums[i] = nums[j]
                i += 1

        return i

# 솔루션 참고 내가 짠 코드랑 차이없음
class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        i = 0
        lenght = len(nums)
        while i < lenght:
            if nums[i] == val:
                nums[i] = nums[lenght-1] # val과 같으면 해당 숫자를 맨 뒤와 바꿔온다.
                lenght -= 1
            else:
                i += 1
        return lenght
