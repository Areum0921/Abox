def solution(n):
    return list(map(int, reversed(str(n))))
#reverse는 원본을 변경, reversed는 원본을 변경하지않음
n=12345
solution(n)
