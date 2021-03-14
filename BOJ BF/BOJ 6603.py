def lotto():
    if(len(out)==6):
        if(99 not in out):
            print(" ".join(map(str, out)))
        return

    for i in range(len(a)):
        if(check[i]==True):
            check[i]=False
            if(len(out)==0):
                out.append(a[i])
            elif(out[len(out)-1]<a[i]):
                out.append(a[i])
            else:
                out.append(99)
            lotto()
            check[i]=True
            out.pop()

while(1):
    a=list(map(int, input().split(" ")))
    if(a[0]==0):
        break
    a.pop(0)
    a.sort()
    out=[]
    result=[]
    check=[True]*len(a)

    lotto()
    print()




