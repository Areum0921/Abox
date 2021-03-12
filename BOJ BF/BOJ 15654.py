N, M=map(int,input().split(" "))
numlist=list(map(int, input().split(" ")))
result=[]
check=[False]*N # 중복 방지 체크
numlist.sort()
def fuc(N, M):
    if(len(result)==M):
        print(' '.join(map(str, result)))
        return

    for i in range(N):
        if(check[i]==False):
            check[i]=True
            result.append(numlist[i])
            fuc(N,M)
            check[i]=False
            result.pop()

fuc(N, M)