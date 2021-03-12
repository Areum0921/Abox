N, M=map(int,input().split(" "))
numlist=list(map(int, input().split(" ")))
result=[]
check=[False]*N # 중복 방지 체크
numlist.sort()
def fuc(N, M):
    if(len(result)==M):
        if(10001 not in result):
            print(' '.join(map(str, result)))
        return

    for i in range(N):
        if(check[i]==False):
            check[i]=True
            if(len(result)==0):
                result.append(numlist[i])
            elif(result[len(result)-1]<numlist[i]):
                result.append(numlist[i])
            else:
                result.append(10001)
            fuc(N,M)
            check[i]=False
            result.pop()

fuc(N, M)