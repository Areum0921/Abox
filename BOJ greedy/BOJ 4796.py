#input ->176ms
#sys.stdin.readline()->120ms
import sys
cnt=0
while(1):
    sum=0
    L,P,V=map(int, sys.stdin.readline().split(" "))
    cnt+=1
    if(L == 0 and P == 0 and V == 0):
        break
    else:
        if(V%P>L):
            sum+=(V//P)*L+L
        elif(V%P<=L):
            sum+=(V//P)*L+(V%P)
    print("Case %d:" %cnt,sum)
