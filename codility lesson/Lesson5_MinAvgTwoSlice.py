# 슬라이스 평균값의 최소값은 반드시 크기가 2 or 3 (최소 2이상이니까, 원래는 1 or 2) 지식 필요.
# 최소 평균값을 찾는건줄 알고 계속 test run 실패.
# return 값은 최소 평균값이 나오는 슬라이스의 시작위치다.

def solution(A):
    avg=9999999
    answer=0
    for i in range(len(A)):
        num1=sum(A[i:i+2])/2
        num2=sum(A[i:i+3])/3

        if i<len(A)-2:
            if avg > num1:
                avg = num1
                answer=i

            if avg > num2:
                avg = num2
                answer=i

        elif i==len(A)-2:
            if avg > num1:
                avg = num1
                answer=i

    return answer




A=[6, 5, 8, 4, 4, 7, 4, 3, 8, 12, 3, 2]
solution(A)