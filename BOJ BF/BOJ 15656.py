N,M =map(int, input().split(" "))
numlist=list(map(int, input().split(" ")))
result=[]
numlist.sort()
def fuc(N,M):
    if(len(result)==M):
        print(" ".join(map(str, result)))
        return

    for i in range(N):
        result.append(numlist[i])
        fuc(N, M)
        result.pop()

fuc(N, M)