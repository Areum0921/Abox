# 개구리는 피보나치 수열 만큼만 점프 가능하다.
# 현재위치에서 개구리는 1칸, 1칸, 3칸, 5칸, 8칸, 13칸.. 이런식으로 밖에 못뛴다.
# 그리고 잎이 있는 곳으로만 뛸 수 있다.
# 문제 자체를 이해하는데 애먹음.

def solution(A):
    A =[1] + A + [1]
    # 출발지와, 목적지는 잎이 있다고 간주한다.
    N = len(A)
    fibo = [1, 1]
    for i in range(2,N):
        fibo.append(fibo[i-1]+fibo[i-2])

    position=[-1]*N # 개구리가 해당 인덱스로 가는 최소 경로비용 저장
    position[0]=0

    for i in range(len(A)):
        if position[i]!=-1: # 점프 가능한 곳
            for j in fibo: # 피보 만큼 점프
                goal = i + j # 위치 i에서 j(피보나치 수열)씩 점프할때
                if goal>=N: # 점프 위치가 N을 벗어나면 점프x
                    # 마지막 인덱스는 N-1이다.
                    break
                if A[goal]==1:# 점프하는 곳에 잎이 있을때
                    if position[goal]==-1: # 방문한적 없는 위치면
                        position[goal]=position[i]+1 # goal까지 이동횟수 + 1회 더한값 넣기
                        # i에서 1번 점프해서 goal로 간 것.

                    elif position[goal] > position[i]+1: # 기존 이동횟수보다 새 이동횟수가 적으면
                        position[goal] = position[i]+1 # 갱신

    # 이 작업을 수행 한 후, position에서 값이 -1인 위치는 도달할 수 없다.
    return position[-1]

A=[0,0,0,0,0]
solution(A)