def solution(left, right):
    answer = 0

    for i in range(left, right + 1):
        cnt = 0
        j = 1
        while j != i+1:
            if i % j == 0:
                cnt += 1 # 약수 개수
            j += 1

        if cnt % 2 == 0: # 약수 개수에따라
            answer += i
        else:
            answer -= i

    #print(answer)
    return answer

left=13
right=17
solution(left,right)