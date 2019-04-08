s=int(input(""))
i=100

if(s<100):
    n=s

elif(s>100):
    n=99
    
    for i in range(s):
        a=i//100;
        b=(i//10)%10
        c=i%10
        print(a,b,c)
        if((a-b)==(b-c)):
            n=n+1

print(n)
