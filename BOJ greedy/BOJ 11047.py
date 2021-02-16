n,k=map(int,input().split())
money=[]

cnt=0
sum=k
for i in range(n):
    money.append(int(input()))

j=n-1
while(j!=-1):
    if (money[j] < k):
        cnt += sum // money[j]
        sum -= (sum // money[j]) * money[j]
    j -=1
    if(sum==0):
        break

print(cnt)