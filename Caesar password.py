def solution(s, n):
    answer = ''

    for i in range(len(s)):

        if (s[i] == " "):
            answer += " "
        elif(s[i].isupper()): #대문자일경우
            answer+=chr(((ord(s[i])+n-65)%26)+65)
        elif(s[i].islower()): #소문자일경우
            answer+=chr(((ord(s[i])+n-97)%26) +97)

    print(answer)
    return answer


s="a B z"
n=25
solution(s, n)