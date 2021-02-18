#우선 순위 큐. 작은순서대로 삭제
#https://python.flowdas.com/library/heapq.html
import sys
import heapq
N=int(input())
num_list = []

sum=0
x=0#임시숫자 저장
y=0
for i in range(N):
    heapq.heappush(num_list, int(sys.stdin.readline()))

if(len(num_list) == 1):
    print(0)

else:
    while(len(num_list)>1):#길이 2부터 비교작업
        x=heapq.heappop(num_list)#제일작은 묶음 꺼내기
        y=heapq.heappop(num_list)#2번째로 작은 묶음 꺼내기
        sum+=x+y
        heapq.heappush(num_list, x+y)
    print(sum)



