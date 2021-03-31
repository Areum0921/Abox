N=int(input())
sceduel=[list(map(int, input().split(" "))) for _ in range(N)]
dp=[0]*(N+1)
pay=0

# i일부터 N일까지 일할때 최대값
for i in range(N-1,-1,-1):
    day, money = sceduel[i] # i일의 상담일, 페이
    if sceduel[i][0] + i > N: # 상담 기간 + 현재날짜 초과하면 현재날짜는 상담 불가
        dp[i]=pay
        continue
    else: # i일에 상담이 가능하다면, i일 상담 비용 + i+day일 비용 or 현재 pay중 max값 저장
        # ex) 백준 예제 입력 1 경우
        # N이 7일때 i가 5면 5일 상담비용 + dp[5+5일상담시필요한시간] 비용 or pay
        # secduel[i][1]+dp[5+2] , pay
        pay=max(sceduel[i][1]+dp[i+day], pay)
        dp[i]=pay

print(pay)

