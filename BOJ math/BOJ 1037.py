# 모든 약수가 입력되는경우
# 2 4 = 8   2*4
# 2 4 8 = 16  4**2
# 2 4 8 16 = 32  4*8
# 2 4 8 16 32 = 64  8**2
# 2 4 8 16 32 64 = 128 8**16
# 진짜 약수개수가 짝수일경우 중앙에있는 2개값 곱해주기 , 홀수일경우 중앙값 1개 제곱
# 규칙을 찾아서 코드짜기
import sys
div=int(sys.stdin.readline())
num=list(map(int, sys.stdin.readline().split(" ")))
num.sort()

check=len(num)#약수가 홀수개인지 짝수개인지

if(check%2==0):#진짜 약수가 짝수개일때
    N=num[check//2]*num[check//2-1]
else:
    N=num[check//2]**2


print(N)