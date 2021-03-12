N,M=map(int,input().split(" "))
check=[0]*N
result=[]
# 이미 들어간 수보다, 작은수가 들어갈경우에 99를 넣어주고 출력때 예외처리
def fuc(N,M):
    if(len(result)==M):
        if(99 not in result):
            print(' '.join(map(str, result)))
        return
    for i in range(N):
        if(len(result)==0):
            result.append(i+1)
        elif(result[len(result)-1]<=i+1):
            result.append(i+1)
        else:
            result.append(99)
        fuc(N, M)
        #print("result23", result)
        result.pop()
        #print("result",result)

fuc(N,M)
