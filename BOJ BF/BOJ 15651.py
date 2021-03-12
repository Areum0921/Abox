N,M=map(int,input().split(" "))

check=[0]*N
result=[]
def fuc(N,M):
    if(len(result)==M):
        print(' '.join(map(str, result)))
        return
    for i in range(N):
        print("^^",i)
        result.append(i+1)
        fuc(N, M)
        print("result23", result)
        result.pop()
        print("result",result)

fuc(N,M)
