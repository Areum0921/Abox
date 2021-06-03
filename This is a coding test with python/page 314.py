# 작은 단위부터 더해나간다.
# 1,2,3,6,14일때
# target 1원 , i = 1원 // 가능
# target = 이전 target + 이전 i = 2원 >= i = 2원 // 가능
# target = 이전 target + 이전 i = 4원 >= i = 3원 // 가능
# target = 이전 target + 이전 i = 7원 >= i = 6원 // 가능
# target = 이전 target + 이전 i = 13원 < i = 14원 // 불가능
# target = 이전 target + 이전 i = 13+14-1 원까지 조합으로 만들 수 있다.

N=int(input())
coin=list(map(int,input().split(" ")))

coin.sort() # 작은 화폐단위부터
target=1

for i in coin:

    if target < i:
        break
    target+=i
print(target)