def check(n):
    return n == n[::-1]
    # 팰린드롬이면 뒤집은거랑 같아야함

def solution(s):
    answer=0
    lens=len(s)
    max=-1
    for i in range(lens): # 문자를 자를 수 있는 모든 경우의 수
        for j in range(i,lens+1): # i번째부터 마지막문자까지
            if(check(s[i:j])):
                if(max<len(s[i:j])):
                    max=len(s[i:j])
    return max
s="abacde"
solution(s)