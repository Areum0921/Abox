# 최대크기 20x20
# 자물쇠 크기를 늘려, 0으로 채워놓고
# 자물쇠 크기가 4x4면 12x12로
# 열쇠를 모든칸에 넣어본다.

def rotate_90(a): # 시계방향으로 90도
    n=len(a)
    m=len(a[0])

    result = [[0]*n for i in range(m)]

    for i in range(n):
        for j in range(m):
            result[j][n-i-1]=a[i][j]

    #print(result)
    return result
def rotate_90_rev(a): # 반시계방향 90도
    n = len(a)
    m = len(a[0])

    result = [[0] * n for i in range(m)]

    for i in range(n):
        for j in range(m):
            print(n-i-1,j)
            result[n - j - 1][i] = a[i][j]
    return result

def check(new_lock): # 자물쇠가 맞는지
    lock_length=len(new_lock) // 3
    for i in range(lock_length, lock_length*2): # 자물쇠가 3x3이면 9x9에서 위치는 3,3 ~ 5,5 (인덱스 기준)
        for j in range(lock_length,lock_length*2):
            if new_lock[i][j]!=1: # 자물쇠 + 키 해서 자물쇠 모든 좌표가 1이면 열 수 있다.
                return False
    return True

def solution(key, lock):
    n = len(lock)
    m = len(key)
    
    new_lock = [[0]* (n*3) for i in range(n*3)]

    for i in range(n): # 확대한 자물쇠에 기존 자물쇠를 가운데에 넣기
        for j in range(n):
            new_lock[i+n][j+n]=lock[i][j]
    for d in range(4): # 4방향으로 key 회전시키기
        key=rotate_90(key)

        for x in range(1,n*2): # 모든칸에 키를 회전해보면서 껴넣기
            for y in range(1,n*2): # 키가 3x3이면 키를 (1,1)~(5,5)까지만 껴보면된다, 이외는 1칸도 겹치지 않기때문에 확인할 필요x
                for i in range(m): # m*m 열쇠 자물쇠에 넣어보기
                    for j in range(m):
                        new_lock[i+x][j+y]+=key[i][j] # 자물쇠 좌표에 key좌표 더해주기
                if check(new_lock)==True:
                    return True

                for i in range(m):
                    for j in range(m):
                        new_lock[i+x][j+y]-=key[i][j]

    return False


key=[[0, 0, 0], [1, 0, 0], [0, 1, 1]]
lock=[[1, 1, 1], [1, 1, 0], [1, 0, 1]]

print(rotate_90_rev(key))
print(solution(key,lock))