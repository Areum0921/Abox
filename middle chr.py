def solution(s):
    answer = ''

    if (len(s) == 1):
        answer = s
    elif (len(s) % 2 == 0):  # 길이가 짝수일때
        answer = s[(len(s) // 2)-1] + s[len(s) // 2 ]
    elif (len(s) % 2 != 0): # 홀수일때
        answer = s[round(len(s) // 2)]

    return answer

s="qwer"
solution(s)