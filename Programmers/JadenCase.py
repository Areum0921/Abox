def solution(s):
    answer = ''
    s=s.split(" ") # 공백으로 나누기
    #print(s)
    for i in range(len(s)):
        for j in range(len(s[i])):
            if(j==0): # 첫문자가 소문자일때 대문자로 바꿔 저장
                #print(s[i][j])
                if(s[i][j].islower()):
                    answer+=s[i][j].upper()
                else:
                    answer+=s[i][j]
            else: # 이후 문자는 대문자일때 소문자로 바꿔 저장
                if s[i][j].isupper():
                    answer+=s[i][j].lower()
                else:
                    answer+=s[i][j]
        answer+=" "

    answer=answer[:-1] # 마지막에 붙는 공백 제거
    return answer

s="3people unFollowed me"
solution(s)