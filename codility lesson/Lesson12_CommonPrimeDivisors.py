# 같은 소인수를 가진 A,B 조합 개수
# 최대 공약수를 이용한다.
from math import gcd

def checkDivisor(x,y):
    while x != 1:
        value = gcd(x,y)
        if value == 1:
            break
        x //= value
        print(x,value)
    # gcd로 계속 나눠서 x가 1이되면 처음 x와 처음 gcd는 같은 prime divisor를 가진다.

    return x == 1 # x == 1이면 true, 아니면 false 반환

def solution(A,B):
    answer=0
    for i in range(len(A)):
        ab_gcd = gcd(A[i],B[i])
        if checkDivisor(A[i],ab_gcd) and checkDivisor(B[i],ab_gcd):
            answer+=1

    return answer

A=[10]
B=[20]
solution(A,B)