from collections import deque
C,B = map(int,input().split())
time = 1
answer = 0
cur = C
q = deque([B])
check = False
while 1:
    if cur > 200000:
        answer = -1
        break
    cur += time
    for _ in range(len(q)):
        num = q.popleft()
        b1 = num + 1
        b2 = num - 1
        b3 = num * 2

        if b1 == cur or b2 == cur or b3 == cur:
            answer = time
            check = True
            break
        else:
            q.append(b1)
            q.append(b2)
            q.append(b3)
    if check==True:
        print("찾음",time)
        break
    time+=1

