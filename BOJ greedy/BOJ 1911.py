#각 웅덩이 시작점부터, 널빤지를 깔아 끝지점을 찾는다.
#널빤지 끝 지점 이후 웅덩이 시작점 찾아 반복
import sys

N, L = map(int,sys.stdin.readline().split(" "))
pool=[[ int(x) for x in input().split() ] for i in range(N) ]
# 인풋 입력받기
pool.sort()

print(pool)

state=0
answer=0

for i in range(N):
    state=max(pool[i][0], state) # 웅덩이 시작점 구하기
    print(state)
    x=pool[i][1]-state#현재 웅덩이 끝 위치 - 시작점 사이의 거리
    count= (x+L-1)//L #(사이의 거리 + 널빤지길이-1)//널빤지길이
    answer +=count# i번째 웅덩이에서 필요한널빤지 개수
    state += count*L #다음 웅덩이 시작점은 현재웅덩이 시작점 + 깔아논 널빤지 끝 다음




print(pool,answer)
