T=int(input(""))
ans=[]
for i in range(T):
    x,y=map(int,input().split())
    sum=0
    a=y-x # x와 y 사이의 거리 
    if a<4: #사이의 거리가 1,2,3이면 최소 이동 횟수와 거리수가같다.
        sum=a
    else :
        b=int(a**0.5) #4미만이 아니면 a의 제곱근 정수만 뽑기
        sum=(b*2)-1 # 규칙에 의해 2b-1개 거리1 1회 거리4 3회 거리9 5회 등등 
        
        if(b!=a**0.5): #제곱근 정수만뽑아낸b랑 a의제곱근(소수포함)같으면 2b-1
            #아니면 a가 b의제곱+b의제곱/2 보다 작으면 회수+1, 크면 회수+2 
            c=b**2
            if(c+int(c*0.5)<a):
                sum+=2
            else:
                sum+=1
    ans.append(sum)
           
for i in ans:
    print(i)
