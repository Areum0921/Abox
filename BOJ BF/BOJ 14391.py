# 자르는 모든 경우를 비트마스크로 해서 모든 경우에 대한 합 구하기
# N x M = 4면 0000~1111 경우를 검사
# 0일때는 세로더하기, 1일때는 가로더하기
def bitmask():
    global max_value
    for i in range(1<<N*M): # 모든 경우에 대해서 (비트마스크로 표현)
        result=0
        for l in range(N): # 가로로 더하기
            rowsum=0
            for k in range(M):
                idx=l*M + k # 1줄로 나열했을때 idx
                # ex
                # 123
                # 312 를 123312로 나열했을때 순서 0,1,2,3,4,5
                if(i & (1 << idx) != 0): # 1 << idx 가 존재할때(1)일때
                    rowsum =rowsum*10 + board[l][k]
                else:
                    result += rowsum
                    rowsum = 0
            result+=rowsum


        for k in range(M): # 세로로 더하기
            colsum = 0
            for l in range(N):
                idx = k + M*l
                # ex
                # 123
                # 312 일때
                # idx 순서 0,3,1,4,2,5
                if(i & (1 << idx) == 0):
                    colsum = colsum*10 + board[l][k]
                else:
                    result += colsum
                    colsum = 0
            result += colsum
        max_value=max(max_value,result)


N, M = map(int,input().split(" "))
board = [list(map(int,input())) for i in range(N)]
max_value = 0
bitmask()
print(max_value)