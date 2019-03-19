#테스트때는 T=int(input("")) 이렇게 입력하면 실패함
for i in range(int(input())): #위 입력방식에서 이렇게만 바꾸니까 pass
    sum=0
    N=int(input(""))
    slist=list(map(str,input().split()))
    for j in range(N):
        a,b=int(slist[j][:-1]),int(slist[j][-1])
        sum+=a**b
    print(f"#{i+1} {sum}")

    

  
   
  
