# len(s)는 n개의 원소일때 n(n+1)//2임
# n의 값을 구하려면 n(n+1) = 2*len(s) , n을 일일이 구하면 시간이 걸릴거같아
# 간단하게 최대 len(s)로 잡음 --> 이것만으로도 시간이 줄음 0~500ms
# 그래도 너무 오래걸려서 검색, 정규식을 사용하라고 한다.
# 이전에 정규식 공부했는데 응용 해보는 문제를 안풀어보니 접근할 생각을 못했다.
# re를 이용하니 속도도 좀 더 빨라지고 코드도 훨씬 간단해진다.

# 0~280ms
import re

def solution(s):
    answer=[]
    s=s.split(",{")
    #print(len(s),s[0],s[1]) # 2 / {{20,111} / 111}} 이렇게 출력된다. 묶음별로 짜르기 가능!
    s=sorted(s, key=lambda x: len(x)) # 길이순으로 정렬, 숫자가 많을수록 길이가 길어진다.

    for i in s:
        num= re.findall("\d+", i)
        for j in range(len(num)):
            if (int(num[j]) not in answer):
                answer.append(int(num[j]))
    #print(answer)
    return answer


"""
이전 코드 0~500ms
def solution(s):
    str=""
    answer=[[] for i in range(len(s))]
    ans=[]
    k=0
    # 등장하는 숫자 모두 리스트로 만들어주기
    for i in s:
        if i.isdigit():
            str+=i
        elif(i==',' or i=='}'):
            if(len(str)>0):
                answer[k].append(int(str))
                str=""
            if(i=="}"):
                k+=1
    answer=answer[:k-1]
    answer=sorted(answer, key=lambda x:len(x)) # 길이가 짧은순으로 정렬
    for i in range(len(answer)):
        for j in range(len(answer[i])):
            if(answer[i][j] not in ans):
                ans.append(answer[i][j])
    print(ans)
"""

s="{{20,111},{111}}"
solution(s)