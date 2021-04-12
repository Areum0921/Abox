n=int(input())
s=list(map(int,input().split(" ")))
check=[False]*123456231
def answer(x,cnt):
    if(x==n):
        check[cnt]=True
        return
    answer(x+1,cnt+s[x])
    answer(x+1,cnt)

answer(0,0)

for i in range(len(check)):
    if(check[i]==False):
        print(i)
        break
