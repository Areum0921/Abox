# 이게 프로그래머스 3단계인게 이상하다.
def solution(n):
    answer = 0
    dp=[0 for i in range(n+1)]
    # dp[i][j] = i칸 까지 가는방법 j개
    dp[1]=1
    if(n>1):
        dp[2]=2
    for i in range(3,n+1):
        dp[i]=(dp[i-2]+dp[i-1])%1234567 # i칸 기준 2칸전, 1칸전
        # 4칸으로 가야하는경우
        # 2칸에서 2칸 이동 or 3칸에도 1칸이동
    answer=dp[n]
    return answer