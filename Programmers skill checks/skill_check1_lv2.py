def solution(s):
    answer = ''
    s=s.split(" ")
    for i in range(len(s)):
        for j in range(len(s[i])):
            if(j==0):
                if(s[i][j].isdigit()==False):
                    answer+=s[i][j].upper()
                else:
                    answer+=s[i][j]
            else:
                if(s[i][j].isupper()):
                    answer+=s[i][j].lower()
                else:
                    answer+=s[i][j]
        answer+=" "
    answer=answer[:-1]
    #print(answer)
    return answer