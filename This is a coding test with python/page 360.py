# 가장 중간에 위치한 집이 최선이다.
# 집의 개수가 짝수면 절반을 나눈뒤 -1 인덱스에 해당하는 위치.
N=int(input())
home = list(map(int,input().split(" ")))
home.sort()

length = len(home)//2

if len(home)%2==0:
    length = length-1

print(home[length])