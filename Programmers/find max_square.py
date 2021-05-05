# dp
def solution(board):
    answer = 1 if 1 in board[0] else 0  # 첫줄에 1이있으면 최소값 1
    # 이렇게 해주지 않고 answer=0으로 시작해놓으면
    # 0,0,0,1
    # 0,0,0,0
    # 1,1~ 검사하기 때문에 이러한 경우에 크기 1짜리가 안잡힌다.
    row = len(board)  # 가로길이
    col = len(board[0])  # 세로길이
    # print(row,col)
    for i in range(1, row):
        for j in range(1, col):
            if (board[i][j]):  # 현재 지점에 사각형이 있으면
                num = min(board[i][j - 1], board[i - 1][j - 1], board[i - 1][j])
                board[i][j] = num + 1
                if (answer < num + 1):
                    answer = num + 1
            # i,j 위,왼쪽, 왼쪽대각선
            # 0 1
            # 1 1 일경우 최소값 0이 있어 만들 수 있는 정사각형 넓이는 최대 (최소값+1)**2

            # 1 1 일경우 최소값 1, 1+1하면 넓이는 2**2
            # 1 1

            # 위,아래,왼쪽대각선이 2면, 아래와 같은 상황인것. 최소값 2에 1더해준것이 현재지점에서 가능한 정사각형 변길이
            # 1 1 1
            # 1 2 2
            # 1 2 1    1-> 2+1

    return answer ** 2