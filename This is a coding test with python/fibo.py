# top down
import time



def fibotd(a):
    if a==1 or a==2:
        return 1
    return fibotd(a-1)+fibotd(a-2)

# bottom up

def fibobu(a):
    f=[1,1]

    for i in range(2,a):
        f.append(f[i-2]+f[i-1])

start=time.time()
fibotd(40)
print(time.time()-start)

start=time.time()
fibobu(40)
print(time.time()-start)