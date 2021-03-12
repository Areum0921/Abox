N,M =map(int, input().split(" "))
numlist=list(map(int, input().split(" ")))
result=[]
numlist.sort()
def fuc(N,M):
    if(len(result)==M):
        if(10001 not in result):
            print(" ".join(map(str, result)))
        return

    for i in range(N):
        if(len(result)==0 or result[len(result)-1]<=numlist[i]):
            result.append(numlist[i])
        else:
            result.append(10001)
        fuc(N, M)
        result.pop()

fuc(N, M)