N=int(input())
triangle=[]
cal_triangle=[[] for i in range(N)]
answer = 0
for i in range(N):
    number = list(map(int,input().split(" ")))
    triangle.append(number)

cal_triangle[0]=triangle[0] # 삼각형 꼭대기
#print(cal_triangle)
for i in range(1,N):
    for j in range(i+1):
        if j==0: # 삼각형 가장 왼쪽
            max_value = cal_triangle[i-1][j]+triangle[i][j]
        elif j==i: # 삼각형 가장 오른쪽
            max_value = cal_triangle[i-1][j-1]+triangle[i][j]
        else:
            max_value = max(cal_triangle[i-1][j]+triangle[i][j],cal_triangle[i-1][j-1]+triangle[i][j])

        cal_triangle[i].append(max_value)

        answer = max(answer,max_value)

print(answer)