N=int(input(""))
cnt=1

num=N

if not(0<=N<=99): # 범위를 벗어나면 종료
    exit()

while True:
    
    a=num//10 #10의자리
    b=num%10 #1의자리
    
    ans=a+b
    
    num=b*10+ans%10#다음숫자는 b가10의자리로와서 b*10 , ans(결과)의 1의자리 ans%10 

    if(num==N): 
        break
    else:
        cnt+=1 
    
print(cnt)

        






