# 규칙 찾기
# n장을 구매하는 최대값은 n장을 구매할수있는 모든 경우의 최소값
# 중복 조합이지만, 이전에 구한 값을 이용해야 시간 통과
# 6장구매시 dp5+1,dp4+2,dp3+3 // dp4 == dp2*2
N = int(input())
price=[0]+list(map(int,input().split(" "))) # 인덱스 n은 n장 뽑는경우
sumn=0

for i in range(1,N+1):
    sumn=99999
    for j in range(1,i//2+1): # 중복조합.(1+3 == 3+1)
        #print("??",price[j],price[i-j],j,i-j,"합",price[j]+price[i-j])
        if(sumn>price[j]+price[i-j]):
            sumn=price[j]+price[i-j]
    if(price[i]>sumn):
        price[i]=sumn
    #print(price)

print(price[N])