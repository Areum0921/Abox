N,M = map(int,input().split())
answer=0

for i in range(N):
    data = list(map(int,input().split())) # 1행씩 입력

    mindata=min(data) # 각 행마다 최소값 저장

    answer=max(answer,mindata) # 현재 결과값과 방금 입력한 행의 최소값중 큰값 저장

print(answer)
