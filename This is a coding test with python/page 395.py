# 도킹가능한 가장 뒷 탑승구 부터 채워보기

# O(n^2)
G = int(input())
P = int(input())
docking=[False]*(G+1)

airplane=[]
cnt=0
for i in range(P):
    airplane.append(int(input()))

for i in range(len(airplane)):
    check=False
    for j in range(airplane[i],0,-1):
        if docking[j]==False:
            docking[j]=True
            check=True
            cnt+=1
            break

    if check==False:
        break


print(cnt,"대 주차 가능")
