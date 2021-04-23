# dp로 접근했었는데 효율성이 안되서 찾아봤더니 N에서 0으로 가는방법이랑 똑같음..
# 2로 나누어지는 지점에서는 순간이동, 아닐경우 한칸
def solution(n):
    cnt=0
    while(n!=0):
        if(n%2==0):
            n=n//2
        else:
            cnt+=1
            n=n-1
    return cnt