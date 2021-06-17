# 못이 A[i] - B[i] 사이에 있으면 판자를 박는다.
# 못이 5고 A=3,5 B=5,10 이면 [3,5], [5,10] 둘다 판자 박음.
# 못은 순차적으로 사용

def plank_check(nail, planks): # 못값, 판자 리스트

    if not planks: # 비어있음
        return -1

    start = 0
    end = 1
    lower = 0 # 판자 인덱스 0
    upper = len(planks)-1 # 판자 마지막 인덱스

    while lower <= upper:
        mid = (lower + upper) // 2 # 정렬된 planks에서 중간인덱스부터 시작
        if planks[mid][start] > nail: # 중간 판자 시작보다 nail값이 더 작으면
            # 못 위치보다 판자 시작 위치가 더 뒤인것.
            upper = mid - 1 # 현재 mid 이전 지점 판자 중에서 가운데로
        elif planks[mid][end] < nail: # 중간 판자 끝보다 nail값이 더 크면
            # 판자 끝 위치보다 못 위치가 더 뒤인것.
            lower = mid + 1 # 현재 mid 이후 지점 판자 중에서 가운데로

        else: # nail이 판자의 끝이나, 시작점과 같으면 못 박기 가능.
            print("mid",mid,planks[mid],nail)
            return mid

    # nail을 판자에 박을 수 없으면 -1 리턴
    return -1

def solution(A,B,C):

    if max(B) < min(C) or min(A) > max(C):
        # 판자의 끝점이 못의 첫점보다 작거나, 판자의 시작점이 못의 끝점보다 크면 못박기 불가능.
        return -1

    plank = sorted(zip(A,B)) # 판자 시작점 순서대로 정렬

    for i in range(len(C)):
        nail = C[i]
        plank_idx = plank_check(nail,plank) # nail 못을 몇번째 판자에 박을 수 있는지
        print("??",plank_idx, plank[plank_idx],plank)

        while plank_idx > -1: # 같은못으로 최대한 박을 수 있을때까지 반복
            print("del",plank, plank_idx)
            del plank[plank_idx] # 해당 판자는 못을 박았으니 판자리스트 삭제
            plank_idx = plank_check(nail,plank) # 기존 못으로 박을 수 있는 판자 찾기

        if not plank: # 판자 다 없앴으면, 모든 판자에 못이 박힌것.
            print(i)
            return i+1
        # 기존 못으로 최대한 판자에 박고 다음 못 탐색
    return -1

A=[1,4,5,8]
B=[4,5,9,10]
C=[4,6,7,10,2]
solution(A,B,C)