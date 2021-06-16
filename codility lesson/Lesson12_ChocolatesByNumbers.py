# N, M 최소공배수 // M  - 1회
from math import gcd
def solution(N,M):

    gcd_num=gcd(N,M)

    return (N*M//gcd_num) - 1



N=10
M=3
solution(N,M)