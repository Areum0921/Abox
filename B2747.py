slist=[]

for i in range(46):
    if(i<2):
        slist.append(i)
    else:
        n3=slist[i-1]+slist[i-2]
        slist.append(n3)
    

N=int(input(""))

print(slist[N])
