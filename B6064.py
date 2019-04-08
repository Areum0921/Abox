def gcd(a, b): #최대 공약수
    while(b !=0):
        temp=a%b
        a=b
        b=temp
    return a

def lcm(a, b): #최소 공배수
  gcd_value = gcd(a, b)
  if (gcd_value == 0): return 0 # 인수가 둘다 0일 때의 에러 처리
  return (a * b) // gcd_value 


T=int(input(""))

for i in range(T):
    M,N,x,y=map(int,input().split())
    while(1):

        if(x>lcm(M,N)): #x, 즉 순서가 M과N의 최소공배수보다 크면 -1
            cnt=-1
            break
        p=x%N #x값이 t1이면 달력에서 다음 x값은 t1+M번째에 t1이나옴 이 t1번째에 y값을 구하려면 %N을 이용
        if(p==0): # x%N이 0이면 y값은 N값과 같음
                #ex)9 12 3 9 일때 x=3이면 y는 3, x가 12면 x%N, 12%12=0이지만 y는 12
                #11,22,33,44,55,66,77,88,99,1 10, 2 11, 3 12, 4 1 순임.
            p=N
            
        if(p==y):#반복해서 해당 x번에 대해 y값이 같으면 x번순서에 찾고자하는 x,y쌍
            cnt=x
            break

        x=x+M
       
           
    print(cnt)

#맨 마지막 해인 M:N는 M과 N의 최소공배수번째 해다.
