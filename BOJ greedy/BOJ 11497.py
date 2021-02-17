def level():
    N=int(input())

    level_list=list(map(int, input().split()))
    level_list.sort()
    print(level_list)
    arry=[0]*len(level_list)
    for i in range(len(level_list)):
        print(i)
        if(i%2==0):
            arry[i//2]=level_list[i]
        else:
            arry[-(i//2)-1]=level_list[i]

    max=arry[0]-arry[-1]

    for i in range(1,len(arry)):
        if(abs(arry[i]-arry[i-1])>max):
            max=abs(arry[i]-arry[i-1])

    print("level",max)

T=int(input())
for i in range(T):
    level()