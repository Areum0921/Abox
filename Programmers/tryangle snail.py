def solution(n):
    answer = []
    tryangle=[[1]*n for i in range(n)]
    #print(tryangle)
    cnt=1
    x,y=0,-1
    for i in range(n): # 첫 i는 아래 방향, 두번째 i는 오른쪽방향, 세번째 i는 위쪽방향 ( 삼각형 그릴때 생각 )
        # n=4
        # 1
        # 2  9
        # 3  10  8
        # 4  5   6  7
        for j in range(i, n):
            if i%3==0:
                y+=1
            elif i%3==1:
                x+=1
            else:
                x-=1
                y-=1
            tryangle[x][y]=cnt
            cnt+=1
            #print(x,y,cnt)

    #for i in tryangle:
        #print(i)
    for i in range(len(tryangle)):
        for j in range(i+1):
            answer.append(tryangle[j][i])

    return answer

solution(4)