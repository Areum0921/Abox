# 1~9는 1자리, 10~99는 2자리, 100~999 3자리, ... 100,000,000은 9자리
N=int(input())
num=10
sum=0

while(1):
    if(N>num-1):
        #print("?",(num-(num//10))*len(str(num-1)),len(str(num-1)))
        #print((num-(num//10)),len(str(num-1)))
        sum+=(num-((num//10)))*len(str(num-1))
        num*=10
    else:
        #print(N-(num//10)+1),len(str(N))
        sum+=(N-(num//10)+1)*len(str(N))
        break

print(sum)