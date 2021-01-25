def solution(strings, n):
    answer = []
    strings.sort()

    answer=sorted(strings, key=lambda x:x[n])# n번째 인덱스 기준으로 정렬

    print(answer)
    return answer
strings=["sun", "bed", "car"]
n=1
solution(strings,n)