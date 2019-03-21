#2007년
dlist=["MON","TUE","WED","THU","FRI","SAT","SUN"]
x,y=map(int,input().split())
date=0
i=1
if(x!=1):
    date+=30
    for i in range(x):
       
        if(i==3 or i==5 or i==7 or i==8 or i==10 or i==12):
            date+=31
        elif(i==2):
            date+=28
        elif(i==4 or i==6 or i==9 or i==11):
            date+=30
    date+=y
else :
    date+=y-1

wd=dlist[date%7]
print(wd)


    
