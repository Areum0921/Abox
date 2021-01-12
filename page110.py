N =int(input())
data=input()
x=1
y=1
count=0
print(data)
while(1):
    if(data[count]=="R"):
        if(y<N):
            y+=1
    elif(data[count]=="L"):
        if(y>1):
            y-=1
    elif(data[count]=="U"):
        if(x>1):
            x-=1
    elif(data[count]=="D"):
        if(x<N):
            x+=1
    count+=1
    if(count==len(data)):
       break

print(x,y)
        
