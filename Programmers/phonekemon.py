def solution(nums):
    answer = 0
    pick = len(nums)//2 # 가져갈수 있는 폰켓몬
    nums = set(nums) # 중복 없이 폰켓몬 종류
    if len(nums)<=pick: # 고를 수 있는 폰켓몬 숫자보다 종류가 더 적으면 최대 종류만큼
        answer=len(nums)
    else: # 고를 수 있는 폰켓몬보다 종류가 더 많으면 고르는 만큼 다른 종류 선택가능
        answer=pick

    return answer