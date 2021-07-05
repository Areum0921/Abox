#bisect 이용
import bisect

answer = -1

N,x = map(int,input().split(" "))
a = list(map(int,input().split(" ")))

left_a = bisect.bisect_left(a,x) # 첫번째 a 인덱스
right_a = bisect.bisect_right(a,x) # 마지막 a 다음 인덱스

print(left_a,right_a)
if right_a - left_a>0:
    answer = right_a - left_a

print(answer)

