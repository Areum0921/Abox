# 블록 관련 문제는 행렬을 전치해보기
# 전치하면 블록 터지는 연산이 쉬워짐.
# 전치 전 : 각 행마다, 전치 후 : 1행 내에서
def find(m,n,board):
    loc = set()

    for i in range(n-1): # 터지는 블록 찾기
        for j in range(m-1):
            if board[i][j]==board[i][j+1]==board[i+1][j]==board[i+1][j+1] and board[i][j]!='e':
                loc |= set([(i,j),(i,j+1),(i+1,j),(i+1,j+1)]) # 없애야할 좌표들 저장

    for i,j in loc:
        board[i][j]=0

    for i,j in enumerate(board):
        print("jj",j)
        empty = ['e'] * j.count(0) # 각 행마다 빈칸
        board[i] = empty + [k for k in j if k != 0] # 터트린 후 블록떨구기
    return len(loc) # 없앤 블록 개수


def solution(m, n, board):
    answer = 0
    board = list(map(list, zip(*board))) # 행렬 전치!!

    while True:
        cnt = find(m,n,board)
        if cnt==0: # 더이상 터트릴 블록이 없을경우
            return answer
        answer+=cnt


m=6
n=6
board = ["TTTANT", "RRFACC", "RRRFCC", "TRRRAA", "TTMMMF", "TMMTTJ"]
solution(m,n,board)