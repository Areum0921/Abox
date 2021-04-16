# 같은 부위 옷이 몇개인지 구한다.
# 3부위 각 3, 4, 2개인경우 안입는 경우를 포함해 4*5*3에서 모두 안입는경우 1을 빼준다.

def solution(clothes):
    answer = 1
    closet = {}  # 옷장
    for i in range(len(clothes)):  # 종류별로 몇개인지
        # print(clothes[i][1])
        if (clothes[i][1] not in closet):
            closet[clothes[i][1]] = 1
        else:
            closet[clothes[i][1]] += 1

    for i in closet:
        # print(closet[i])
        answer *= closet[i] + 1  # 안입는 경우도 포함
    answer = answer - 1  # 모두 안입는경우 제외
    return answer