def solution(s):
    answer = ''
    string1 = s.split(" ")  # 공백기준으로 단어 나누기

    for i in range(len(string1)):
        for j in range(len(string1[i])):
            if (j % 2 == 0 and string1[i][j].islower() == True):

                answer += string1[i][j].upper()
            elif (j % 2 != 0 and string1[i][j].isupper() == True):

                answer += string1[i][j].lower()
            else:
                answer += string1[i][j]
        if(i<len(string1)-1):
            answer+=" "
    print(answer)
    return answer

s="try hello world"
solution(s)