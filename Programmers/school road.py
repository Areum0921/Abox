# 최단 경로의 개수
# m,n의 최대값은 각각 100
# 100 * 100 = 10000
# 좌표가 헷갈릴때는 그려서 해보자.
def solution(m, n, puddles):
    answer = [[0]*(m+1) for i in range(n+1)]
    answer[1][1]=1
    # 좌표 i,j는 (i-1,j)나 (i,j-1)에서 올수있다.
    for i in range(1,n+1):
        for j in range(1,m+1):
            if i==1 and j==1:
                continue
            if [j,i] in puddles: # 물웅덩이가 있는곳은 0으로 그러면 주변 경로 구할때 반영x
                answer[i][j]=0
                # puddles 좌표 주의 맨마지막 지점 m,n임 반대로 넣어줘야 정상작용
            else:
                answer[i][j]=(answer[i-1][j] + answer[i][j-1])%1000000007
    for i in answer:
        print(i)
    return answer[n][m]

m=4
n=3
puddles = [[2,3]]
solution(m,n,puddles)