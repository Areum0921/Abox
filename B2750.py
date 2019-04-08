T=int(input(""))
slist=[]
for i in range(T):
    s=int(input())
    slist.append(s)

slist.sort()

for i in range(len(slist)):
    print(slist[i])
