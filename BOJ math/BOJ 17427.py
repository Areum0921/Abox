# g(10)은 10이하 숫자들의 약수의 합.
# g(10) = 1*10 + 2*5 + 3*3 + 4*2 + 5*2 + 6*1 + 7*1 + 8*1 + 9*1 + 10*1
# 10이하 자연수들을 A라 했을때 A*(10//A) , A=1~10
N=int(input())
answer=0
for i in range(1,N+1):
    answer+=i*(N//i)

print(answer)