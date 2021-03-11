# combinations 사용
from itertools import combinations

N, M=map(int, input().split(" "))
num=[str(i+1) for i in range(N)]
for i in list(map(' '.join, combinations(num, M))):
    print(i)
