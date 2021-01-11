# N개의 숫자가 주어지고, 총 M번 더하기,연속으로 K번을 초과하여 더할 수 없을때
# 가장 큰 수 만들기.

N,M,K=map(int,input().split())

data = list(map(int,input().split()))

data.sort()

maxnum=data[N-1]
smaxnum=data[N-2]

answer=0
c=0
while(True):
    
    for i in range(K):
        if c==M:
            break
        answer+=maxnum
       
        c+=1
    if(M==c):
        break
    answer+=smaxnum
    c+=1

print(answer)
    
            
    
