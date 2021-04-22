def solution(n):
    answer = 0
    binary=bin(n)[2:]# 0b 없애고 저장
    #print(binary)
    count=binary.count('1') # 해당 이진수의 1 개수
    #print(count)
    while(1):
        n+=1
        binary2=bin(n)[2:] # 비교할 숫자의 이진수
        count2=binary2.count('1') # 비교할 숫자의 이진수의 1 개수
        if(count==count2):
            answer=n
            break
    return answer