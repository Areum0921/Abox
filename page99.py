N,K = map(int,input().split())
count=0
while(1):
    print(N)
    if(N%K==0):
        N=N//K
        count+=1
    elif(N==1):
        break
    else:
        count+=1
        N-=1
        


print(count)
    
