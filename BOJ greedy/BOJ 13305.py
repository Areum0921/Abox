import sys

N=int(sys.stdin.readline())#도시 개수
N_dis=list(map(int,sys.stdin.readline().split()))#도시간의 거리
price=list(map(int,sys.stdin.readline().split()))#도시별 기름 가격

dis=N_dis[0] # 처음가야할 거리
p=price[0] # 현재 가격
total=0 #현재까지 비용

for i in range(1,N):
    print(i, dis, p,total)
    if(i==N-1): # 마지막 도시만 남은 경우
        total += dis * p
        break
    if(p<price[i]):#다음마을이 더 비쌀때
        dis+=N_dis[i] # 현재 가격으로 가야할 거리 합하기
    else:#다음마을이 더쌀때
        total += dis * p
        p=price[i]
        dis=N_dis[i]

print(total)



