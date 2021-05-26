# U일때 x좌표 -1
# D일때 x좌표 +1임
# 좌표 예시
# (1,1) (1,2) (1,3) (1,4)   → R, ← L, ↑ U, ↓ D
# (2,1) (2,2) (2,3) (2,4)
# (3,1) (3,2) (3,3) (3,4)
# (4,1) (4,2) (4,3) (4,4)
def solution(n,command):
    loc=[1,1] # 시작 좌표 , 가장 왼쪽 위

    for i in command:
        print(loc, i)
        if i == 'R': #
            if loc[1]<n:
                loc[1]+=1
        elif i=='L':
            if loc[1]>0:
                loc[1]-=1
        elif i=="D":
            if loc[0]<5:
                loc[0]+=1
        elif i=='U':
            if loc[0]>1:
                loc[0]-=1

    print(loc[0],loc[1])



n=5
command="RRRUDD"
solution(n,command)