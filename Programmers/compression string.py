#문자열 길이의 절반까지 잘라서 확인하면됨
#예시로 11글자 짜리를 6글자로 나누면 6/5글자가되는데 서로 겹쳐서 중복 시킬 수 없음

def solution(s):
    answer = len(s)  # 압축이 하나도 안될때 최대길이

    for i in range(1, len(s) // 2 + 1):
        p = s[:i]  # 처음문자열
        total = "" # 압축문자 저장용
        cnt=1 # 해당문자는 1개있는것부터 시작
        for j in range(i, len(s), i): # i개씩 끊어서
            if (p == s[j:j + i]):
                print("문자열 비교",p,s[j:j+i])
                cnt += 1
            else:
                print("다른문자 발견",cnt, p,s[j:j+i])
                if (cnt > 1): # 똑같은 문자있으면
                    # 3ab , 2ab
                    total+=str(cnt)+p # ab가 3개면 3ab 식으로 더해주기
                else:
                    total+=p # 겹치는게없다면 현재 비교 문자열인 p 더해주기
                p = s[j:j+i] # 비교문자열 갱신
                cnt=1 # 다른문자로 다시 탐색시작 cnt 초기화
                #print('새로운 문자열',p)
        if(cnt>1):
            total += str(cnt) + p
        else:
            total +=p
        #print("압축 길이",i,"개씩 자를때",total)
        if(answer>len(total)): # i개씩 잘랐을때 압축된 문자열의 길이가 기존보다 작으면 갱신
            answer=len(total)

    print(answer)
    return answer

s="abcabcdede"
solution(s)
