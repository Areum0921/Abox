# 규칙
# 2*2 = 2, 2*3 = 3, 2*4 = 5, 2*5 = 8, 2*6 = 13
# 피보나치랑 비슷, 재귀 호출수 제한..

d=[0,1,2]
N=int(input())
for i in range(3,N+1):
    d.append(d[i-1]+d[i-2])

print(d[N]%10007)




