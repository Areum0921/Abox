# nums 숫자들로 만들 수 있는 합을 구해 소수인지 판별한다.
# 분명히 맞는데 안되서 질문글보니까, 같은 sum이여도 조합이 다르면 카운트 따로 체크 해야함

from itertools import combinations

def solution(nums):
    answer = 0
    nums.sort()  # 정렬하기
    era = [0] * (sum(nums[-3:]) + 1)  # 에라토스테네스의 체, 최대 숫자 정렬후 뒤에서 3개 더했을경우
    for i in range(2, len(era)):
        if era[i] == 0:
            for j in range(i * 2, len(era), i):
                era[j] = 1  # 소수가 아닌 수 표시

    comb = []  # 3개씩 더했을때 만들 수 있는 수
    for i in combinations(nums, 3):  # 3개를 뽑아 만들 수 있는 수
            comb.append(sum(i))
    print(comb)
    for i in comb:
        if era[i] == 0:
            answer += 1
    print(comb,era,answer)
    return answer

solution([1,2,3,4])