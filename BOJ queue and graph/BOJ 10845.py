import sys
N=int(sys.stdin.readline())
queue=[]
for i in range(N):
    a=sys.stdin.readline().strip() # .strip() 개행문자 제거
    if('push' in a):
        x,y=a.split(" ")
        queue.append(y)
    elif(a=='pop'):
        if(len(queue)==0):
            print(-1)
        else:
            print(queue[0])
            queue.pop(0)
    elif(a=='size'):
        print(len(queue))
    elif(a=='front'):
        if(len(queue)==0):
            print(-1)
        else:
            print(queue[0])
    elif(a=='back'):
        if(len(queue)==0):
            print(-1)
        else:
            print(queue[-1])
    elif(a=='empty'):
        if(len(queue)==0):
            print(1)
        else:
            print(0)

