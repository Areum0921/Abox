# 구현 디테일

def solution(rows, columns, queries):
    board =[[(j-1) * columns + i for i in range(1,columns+1)] for j in range(1,rows+1)]
    # 행, 열 개수 확인 잘하기
    answer = []

    for x1,y1,x2,y2 in queries: # 각 테두리마다 제일 작은값을 저장해놓으면 모서리 부분 값 저장 가능
        temp = board[x1-1][y2-1] # 오른쪽 상단 모서리값
        min_num = 100000 # 회전결과에서 가장 작은값 저장

        min_num = min(min(board[x1-1][y1-1:y2-1]),min_num) # 윗 테두리에서 가장 작은값 찾기
        board[x1-1][y1:y2] = board[x1-1][y1-1:y2-1] # 오른쪽으로 한칸씩 옮기기

        for i in range(x1,x2): # 왼쪽 테두리, 위로 한칸씩
            min_num = min(board[i][y1-1], min_num)
            board[i-1][y1-1] = board[i][y1-1]


        min_num = min(min(board[x2-1][y1:y2]),min_num)
        board[x2 - 1][y1 -1:y2 -1] =  board[x2-1][y1:y2] # 아래쪽 테두리 왼쪽으로 한칸씩

        for j in range(x2-1,x1,-1): # 오른쪽 테두리 아래로 한칸씩
            min_num = min(board[j-1][y2-1],min_num)
            board[j][y2-1] = board[j-1][y2-1]

        board[x1][y2-1]= temp

        for i in board:
            print(i)
        print()
        answer.append(min(min_num,temp))

    print(answer)
    return answer

rows = 3
columns = 3
queries = [[1,1,2,2],[1,2,2,3],[2,1,3,2],[2,2,3,3]]
solution(rows,columns,queries)