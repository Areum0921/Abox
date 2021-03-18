N, M =map(int,input().split(" "))
board=[list(map(str, input())) for _ in range(N)]
answer=[]

def solution():
    for i in range(N-7):
        for j in range(M-7):
            num1=0 # 시작위치 색깔 B, W 2가지 경우
            num2=0
            for k in range(i, i+8): # i = 0~N-7
                for l in range(j, j+8): # j = 0~M-7
                    if((k+l)%2==0): # 현재 위치가 짝수일때
                        if(board[k][l] =='B'): num1+=1 # B로 시작하는 경우
                        if(board[k][l] =='W'): num2+=1 # W로 시작하는 경우
                    else:
                        if (board[k][l] == 'W'): num1 += 1 # B로 시작하는 경우 좌표 합이 홀수
                        if (board[k][l] == 'B'): num2 += 1 # W로 시작하는 경우 좌표 합이 짝수
            answer.append(num1)
            answer.append(num2)

solution()
print(min(answer))

