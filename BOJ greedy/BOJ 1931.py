N=int(input())
time_table=[[0]* 2 for _ in range(N)] #회의 시간표

for i in range(N):
    s,c=map(int,input().split(" "))
    time_table[i][0]=s
    time_table[i][1]=c

print(time_table)
ctime=sorted(time_table,key=lambda x: (x[1], x[0]))
#끝나는 시간이 빠른순으로, 끝나는 시간이 같다면 시작시간이 빠른순

start=ctime[0][0] #첫회의 시작시간
end=ctime[0][1]#첫회의 끝나는시간
cnt=1 #회의 갯수(첫회의는 위에서 먼저 카운트)
for i in range(1,len(ctime)):

    if end<=ctime[i][0]: #이전 회의시간의 끝시간보다 다음 회의 시작시간이 같거나 이후일때
        start=ctime[i][0]
        end=ctime[i][1]
        print("다음 회의를 시작합니다.", "시작시간: ", start, "종료시간 :", end)
        cnt+=1

print(cnt)
