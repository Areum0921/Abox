#pypy3,python3 메모리초과 - 실패
import sys
M=int(sys.stdin.readline())
cal=[list(map(str, sys.stdin.readline().split())) for _ in range(M)]
S=[]
for i in range(M):

    if(cal[i][0]=='add'):
        S.append(cal[i][1])
    elif(cal[i][0]=='remove'):
        if(cal[i][1] in S):
            S.remove(cal[i][1])
    elif(cal[i][0]=='check'):
        if(cal[i][1] in S):
            print(1)
        else:
            print(0)
    elif (cal[i][0] == 'toggle'):
        if(cal[i][1] in S):
            S.remove(cal[i][1])
        else:
            S.append(cal[i][1])
    elif(cal[i][0]=='all'):
        S=[str(i) for i in range(1,21)]
    elif(cal[i][0]=='empty'):
        S=[]
