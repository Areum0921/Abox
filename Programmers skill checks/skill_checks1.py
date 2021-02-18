#에라토스테네스 채
def solution(n):
    era = [True] * (n+1)
    for i in range(2, n):
        print(i)
        if(era[i]==True):
            for j in range(i + i, n+1, i): #i의 배수는 소수가 아님
                era[j] = False

    answer = era.count(True)-2 # 0,1은 소수가아님
    return answer

solution(10)