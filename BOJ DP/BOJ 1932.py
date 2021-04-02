import sys
n=int(sys.stdin.readline())
tryangle=[list(map(int,sys.stdin.readline().split(" "))) for _ in range(n)]
empty=tryangle[::] # 원본 지키면서 empty값 갱신시킬수 있도록

for i in range(1,n):
    for j in range(len(empty[i])):
        if(j==0): # 삼각형 n번째 줄의 첫부분일때
            empty[i][j]=empty[i][j]+empty[i-1][j]
        elif(j==len(empty[i])-1): # 삼각형 n번째 줄의 마지막일때
            empty[i][j]=empty[i][j]+empty[i-1][j-1]
        else:
            empty[i][j]=empty[i][j]+max(empty[i-1][j-1],empty[i-1][j])

print(max(empty[n-1]))
