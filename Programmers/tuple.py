# 통과했지만 시간이 너무 오래걸림 200ms ~ 700ms....
def solution(s):
    answer=[]
    ans=[[] for i in range(len(s))]

    # 리스트로 만들기
    k=0
    str=""
    for i in range(len(s)):
        #print(i, ans)
        if s[i]=="}":
            if(len(str)==0):
                break
            if(len(str)>0):
                ans[k].append(int(str))
                str=""
            k+=1
        elif s[i].isdigit():
            str+=s[i]
        elif s[i]=="," and s[i+1]!='{':
            if(len(str)>0):
                ans[k].append(int(str))
                str=""


    #print(ans[:k])
    ans=ans[:k]
    #print("???", ans)
    ans=sorted(ans, key=lambda x:len(x)) # 길이가 짧은순으로 앞으로 오기
    for i in range(len(ans)):
        for j in range(len(ans[i])):
            if(ans[i][j] not in answer):
                answer.append(ans[i][j]) # 없는 숫자 넣어주기
    #print(answer)
    return answer

s="{{123}}"
solution(s)