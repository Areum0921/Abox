# 비트마스크 써도 시간이 오래걸린다.
# x의 제한이 20임을 이용해 배열도 가능하다.
# 4336ms -> 3888ms 조금줄었다. (python3)
# pypy3가 통과못하는 이유는 python3에비해 메모리를 더 많이 써서 그렇다고 한다.
import sys
M=int(sys.stdin.readline())
S=[0]*20 # 이진법처럼 생각하기

for _ in range(M):
    command = sys.stdin.readline().strip().split(" ")
    if(command[0] == "add"):
        S[-int(command[1])] = 1 # int(command[1])가 3이면 오른쪽부터해서 3번째임을 이용
    elif(command[0] == "remove"):
        S[-int(command[1])] = 0
    elif(command[0] == "check"):
        if(S[-int(command[1])] == 1):
            print(1)
        else:
            print(0)
    elif (command[0] == "toggle"):
        if (S[-int(command[1])] == 1):
            S[-int(command[1])] = 0
        else:
            S[-int(command[1])] = 1
    elif(command[0] == "all"):
        S = [1]*20 # 1~20까지
    elif(command[0] == "empty"):
        S = [0]*20
