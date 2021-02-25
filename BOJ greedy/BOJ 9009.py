import sys
#입력방식을 input -> sys.stdin.readline 바꾸니까
# 260ms -> 164ms로 줄음
def find_fibo(x): # x이하까지 피보나치수 구하기
    fibo=[0,1]
    i=2
    while(1):
       fibo.append(fibo[i-2]+fibo[i-1])
       if(fibo[i]>x):
           fibo.pop(-1)
           break
       i+=1
    j=-1
    sum=0
    use_num=[]
    print(fibo)
    while(1):
        if(sum+fibo[j]<=x): #큰숫자별로
            sum+=fibo[j]
            use_num.append(fibo[j])
        j-=1
        if(sum==x):
            break
    print(use_num)

    for i in range(len(use_num)):
        print(use_num[-i-1],end=" ")
    print()

T=int(sys.stdin.readline())
for i in range(T):
    find_fibo(int(sys.stdin.readline()))
