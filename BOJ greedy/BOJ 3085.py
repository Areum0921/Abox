# a[0][0],a[0][1]=a[0][1],a[0][0] 인접한 사탕 위치 변경할때 안됌..
# 입력방식을 ["YCPZY","CYZZP"] 에서 ["Y","C","P","Z",Y"] 이런식으로 바꿔주니까 변경됌
import sys
N = int(sys.stdin.readline())

a=[list(map(str, input())) for _ in range(N)]

result=0

def find(a): # 연속된 사탕찾기
    cnt=0
    for i in range(N):
        cnt_row=1
        cnt_col=1
        for j in range(1,N):
            if(a[i][j]==a[i][j-1]): #가로방향 체크
                cnt_row+=1
            else:
                cnt = max(cnt, cnt_row) #현재 최대치와 새로 카운트한 개수 비교
                cnt_row=1

            if(a[j][i]==a[j-1][i]): #세로방향 체크
                cnt_col+=1
            else:
                cnt = max(cnt, cnt_col)
                cnt_col = 1
        cnt=max(cnt,cnt_col,cnt_row)# 현재 열이나 행의 마지막까지 셌을경우 else조건 발동x, 그래서 다시한번 더 비교
        # N이 5일때 a[0][4],a[0][5]비교 이후 다음 열,행으로 가기전에
    return cnt

for i in range(N):
    for j in range(1,N):
        # 같은색일경우에는 서로 위치 변경해도 똑같음.
        if(a[i][j] != a[i][j-1]):
            a[i][j],a[i][j-1]=a[i][j-1],a[i][j] # 가로방향으로 2개 서로바꾸기
            result=max(result,find(a)) # 바꾸고, 최대 사탕개수 체크하기
            a[i][j], a[i][j - 1] = a[i][j - 1], a[i][j] #원래대로 돌려놓기

        if(a[j][i] != a[j-1][i]):
            a[j][i],a[j-1][i]=a[j-1][i],a[j][i]
            result=max(result,find(a))
            a[j][i], a[j - 1][i] = a[j - 1][i], a[j][i]#원래대로 돌려놓기


print(result)






