# 비트마스크사용하기
# pypy3 -> 메모리 초과, python3 통과
import sys
M=int(sys.stdin.readline())
S=0

for _ in range(M):
    cal = sys.stdin.readline()
    command=cal.split()[0]

    if(command == "add"):
        S |= 1<<int(cal.split()[1]) # 있으면 추가, 없으면 그대로
    elif(command == "remove"):
        S &= ~(1<<int(cal.split()[1])) # 있으면 ~로 지우기
    elif(command == "check"):
        if(S & (1<<int(cal.split()[1]))):
            print(1)
        else:
            print(0)
    elif(command == "toggle"):
        S ^= (1<<int(cal.split()[1])) # 있으면 0으로, 없으면 1로
    elif(command == "all"):
        S = (1<<21)-1 # 1~20까지
    elif(command == "empty"):
        S = 0
