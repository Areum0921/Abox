def solution(str1, str2):
    str1=str1.lower() # 대문자 == 소문자이므로 소문자로통일
    str2=str2.lower()

    str1_arr=[] # 쪼갠 문자열 저장
    str2_arr=[]

    str_split=""
    for i in str1: # 문자열 쪼개기
        str_split+=i
        if(len(str_split)==2):
            if(str_split[0].isalpha() and str_split[1].isalpha()): # 둘다 문자일때만 추가
                str1_arr.append(str_split)
            str_split=str_split[1]

    str_split=""
    for i in str2: # 문자열 쪼개기
        str_split+=i
        if(len(str_split)==2):
            if(str_split[0].isalpha() and str_split[1].isalpha()): # 둘다 문자일때만 추가
                str2_arr.append(str_split)
            str_split=str_split[1]
    print(str1_arr,str2_arr)
    intersection=[]
    if len(str1_arr) < len(str2_arr): # intersection
        for i in str2_arr: # str2_arr원소를 하나씩 꺼낸다
            if i in str1_arr: # 만약 해당 원소가 str1_arr에도 있다면
                intersection.append(i) # 교집합이고
                str1_arr.remove(i) # str1_arr에서 해당 원소를 제거한다
    else:
        for i in str1_arr:
            if i in str2_arr:
                intersection.append(i)
                str2_arr.remove(i)

    inter = len(intersection) # 교집합
    union = (str1_arr + str2_arr) # 리스트 하나에서 교집합제외 하고 + 나머지 원소끼리 더해준다.
    print(intersection,union)
    if union==0:
        return 65536
    answer= int(inter/union * 65536)
    return answer

str1='aaa+bb'
str2='aaaa+cc'
solution(str1,str2)