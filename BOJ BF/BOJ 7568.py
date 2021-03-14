N=int(input())

x=[list(map(int, input().split(" "))) for _ in range(N)]
total=[1]*N # 자기보다 덩치 큰사람이 없으면 1등이기때문에
sum=0
def compare_xy(a): # 자기보다 덩치큰사람 뽑아내기
    global sum
    if(sum==N-1 or a>N-1):
        sum=0
        print(' '.join(map(str, total)))
        return

    for i in range(N):
        sum+=1
        #print(a,sum,total)
        #print(x[a][0],x[a][1],x[i][0],x[i][1])
        if(x[a][0]<x[i][0] and x[a][1] <x[i][1]): # 자신보다 덩치큰사람 수
            total[a]+=1
    compare_xy(a+1) # 순위비교 끝나면 다음사람 기준으로 덩치 비교
    sum=0


compare_xy(0)


