from bisect import bisect_left,bisect_right

# bisect_left(arr,value) value값의 위치 인덱스
# bisect_rigth(arr,value) value값 다음 위치 인덱스

def cal(arr,left_value,right_value): # a값에 해당하는 개수

    left_idx = bisect_left(arr,left_value)
    right_idx = bisect_right(arr,right_value)

    return right_idx - left_idx

arr = [[] for _ in range(10001)]
reversed_arr = [[] for _ in range(10001)]

def solution(words, queries):
    answer=[]
    for i in words:
        arr[len(i)].append(i) # arr 인덱스 값 n에는 n글자인 단어들 넣기
        reversed_arr[len(i)].append(i[::-1]) # 위와 마찬가지 단, ?가 앞에나오는 경우를 대비해 뒤집어 저장

    for i in range(10001): # 개수만 구하면 되므로 사전순으로 해서 bisect 이용하여 구하기
        arr[i].sort()
        reversed_arr[i].sort()

    for q in queries:
        if q[0]=="?":
            ans = cal(reversed_arr[len(q)],q[::-1].replace("?",'a'),q[::-1].replace("?",'z'))
            # reversed 경우 뒤 알파벳이 앞으로 나오기때문에 가장 끝 알파벳 z를 맨앞에, 가장 앞 알파벳 a를 맨뒤에 붙여 bisect로 계산
            # ????o 같은경우 aaaao ~ zzzzo 사이를 검색한다.
        else:
            ans = cal(arr[len(q)],q.replace("?","a"),q.replace("?","z"))

        answer.append(ans)
    return answer

words=["frodo", "front", "frost", "frozen", "frame", "kakao"]
queries=["fro??", "????o", "fr???", "fro???", "pro?"]
print(solution(words,queries))