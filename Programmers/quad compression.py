# 4분할 후, 각 네모의 왼쪽 상단 좌표 기준
# 네모가 1개있다고 가정하고 재귀 시작.
def check(x,y,n,answer):
    start_value = arr[x][y] # 각 네모의 시작 좌표에 있는 숫자 0 or 1
    for i in range(x,x+n):
        for j in range(y,y+n):
            if arr[i][j]!=start_value: # 시작좌표 숫자와 다르면 쪼개기
                # 예를들어 처음 네모가 가로세로 길이가 8일때, 오른쪽상단 네모 (시작점 0,4) 쿼드 합병불가하면
                # 이것을 다시 4분할한다. 그럼 각 왼쪽상단 좌표는 (0,4),(0,6),(2,4),(2,6)을 기준으로 다시 확인
                half = n//2
                check(x,y,half,answer)
                check(x,y+half,half,answer)
                check(x+half,y,half,answer)
                check(x+half,y+half,half,answer)
                return
    answer[start_value]+=1

def solution(arr):
    answer = [0, 0]
    n = len(arr)
    check(0,0,n,answer)

    return answer

arr=[[1,1,1,1,1,1,1,1],[0,1,1,1,1,1,1,1],[0,0,0,0,1,1,1,1],[0,1,0,0,1,1,1,1],[0,0,0,0,0,0,1,1],[0,0,0,0,0,0,0,1],[0,0,0,0,1,0,0,1],[0,0,0,0,1,1,1,1]]
solution(arr)