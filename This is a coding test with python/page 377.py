N = int(input())
schedule=[]
pay =[0] * (N+1) # 해당 일자의
max_val = 0
for i in range(N):
    x,y = map(int,input().split())
    schedule.append([x,y])


for i in range(N-1,-1,-1): # 마지막날부터 계산, 각 날짜부터 상담을 시작한다 했을때 최대 비용 저장해나감.
    day, cost = schedule[i][0],schedule[i][1] # i+1일 상담시 걸리는시간, 비용

    time = day+i # i+1 일째 상담이 끝나는 시점
    
    if day + i <= N: # 기간안에 상담을 끝낼 수 있으면
        pay[i] = max(max_val,pay[time]+cost) # 최고가격 or 현재 상담 가격 + 이후 일정 최대 누적 가격
        max_val = pay[i]
    else:
        pay[i] = max_val

    print(pay)

print(max(pay))

