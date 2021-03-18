# 이전에 배운 lambda를 이용해 정렬해야하는줄 알았다.
# 그냥 sort 함수 써도 첫인덱스 기준정렬 -> 그다음 인덱스 기준 정렬 인듯..

import sys
N=int(sys.stdin.readline())
numlist=[list(map(int, sys.stdin.readline().split(" "))) for _ in range(N)]
#answer=sorted(numlist, key=lambda x:(x[0])) # x[0]기준으로 오름차순 후, x[1]기준으로 오름차순
numlist.sort()

for i in numlist:
    print(' '.join(list(map(str, i))))
