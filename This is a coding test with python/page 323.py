def solution(s):
    result=999999999
    length = len(s)//2 # 길이의 절반까지만 확인하면됨 (압축 성질)
    if len(s)==1: # 문자열 1개일때
        return 1
    for i in range(1,length+1):
        answer = '' # n개씩 자르는경우 압축결과
        x = s[:i] # 초기 문자열

        cnt=1 # 압축 횟수
        for j in range(i,len(s),i): # 0~i, i~i+i
            if x == s[j:j + i]:  # 비교할 문자열과 같으면 압축

                cnt += 1
            else:  # 다르면 압축횟수+문자열 저장
                if cnt > 1: # 압축횟수가 2이상일때
                    answer+=str(cnt)+x
                    cnt=1
                else:
                    answer+=x
                x=s[j:j+i]#비교문자열 변환
        if cnt>1:
            result=min(result,len(answer+str(cnt)+x))
        else:
            result=min(result,len(answer+x))

    return result
s="aabbaccc"
solution(s)