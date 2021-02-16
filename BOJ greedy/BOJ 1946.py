#input을 sys.stdin.readline()로 바꿔줬더니
# 7640ms -> 5948ms
import sys
T=int(sys.stdin.readline())
for i in range(T):
    N=int(input())
    ranking = [[0] * 2 for _ in range(N)]
    for i in range(N):
        x,y=map(int, sys.stdin.readline().split(" "))
        ranking[i][0]=x
        ranking[i][1]=y
    ranking.sort()
    cnt = 1  # 서류심사1등은 무조건 고용
    first=ranking[0][1] #서류심사 1등의 인터뷰점수가 기준
    for j in range(1,len(ranking)):#현재 기준이 되는 지원자의 인터뷰점수보다 등수가높다면 합격
        if(first>ranking[j][1]):
            cnt+=1
            first=ranking[j][1] # 합격기준 인터뷰등수 업데이트

    print(cnt)


