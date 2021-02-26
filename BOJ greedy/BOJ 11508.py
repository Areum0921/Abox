N=int(input())
set_N=[]
for i in range(N):
    set_N.append(int(input()))
set_N.sort(reverse=True)#비싼순대로 3개씩묶기

sum=0

for i in range(len(set_N)):#3개씩묶였을때 묶음마다 마지막 가격 더하지않기
    if(i%3!=2):
        sum+=set_N[i]

print(sum)