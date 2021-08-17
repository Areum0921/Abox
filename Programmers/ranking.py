# 선수의 수는 100명이하, 경기수는 4500 -> 충분히 작다.
# 플로이드워셜 jk
def solution(n, results):
    answer = 0

    game = [[0] * (n + 1) for _ in range(n + 1)]

    for i in range(n):
        game[i][i]=0

    for j in results:
        game[j[0]][j[1]] = 1 # 승리
        game[j[1]][j[0]] = -1 # 패배

    for i in range(1, n + 1):
        for j in range(1, n + 1):
            for k in range(1, n + 1):
                if game[j][k]==0: # i와 j의 승패를 모를때. 플로이드워셜 순서 중요. jk!! 순서에따라 결과라 다를수있음
                    if game[j][i]== 1 and game[i][k]==1: # i가 k를 이기고, k가 j를 이기면 i는 j를 이긴다.
                        game[j][k]=1
                    elif game[j][i]== -1 and game[i][k]== -1: # 지는경우
                        game[j][k]=-1

    for i in range(1, len(game)):
        print(game[i][1:])
        if game[i][1:].count(0) == 1:  # 0이 한개라는건 자기자신 외 다른 선수와의 승패결과가 모두 존재.
            answer += 1

    return answer

n=5
result = [[1, 4], [4, 2], [2, 5], [5, 3]]
solution(n,result)