n=int(input(""))
ans=0
cent=0

if(n%5==0): #5의 배수 일때
    ans+=int(n/5)
elif(n==1 or n==3):#거스름돈 못줄때
    ans-=1
else:
    while(n%5!=0):
        n-=2
        cent+=1
    a=int(n/5)
    ans+=a+cent
    
print(ans)
