a=[1,2,3]
out=[]
answer=[]
cnt=0
cnt2=0
def solution(n,k):
    global cnt,cnt2
    if(sum(out)==n or len(out)==n):
        if(sum(out)==n):
            cnt+=1
        if(sum(out)==n and cnt==k):
            cnt2+=1
            print('+'.join(map(str, out)))
        return


    for i in range(3):
        out.append(a[i])
        solution(n,k)
        out.pop()

n,k=map(int,input().split(" "))
solution(n,k)
if(cnt2==0):
    print(-1)


