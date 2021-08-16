def solution(msg):
    answer = []
    dictionary = {}

    for i in range(26):
        dictionary[chr(65+i)]=i+1
    i=0
    idx = 27 # 사전에 추가될 문자열 인덱스
    word=''
    while i!=len(msg):
        word += msg[i] # 단어 늘리기
        if word not in dictionary: # 없는 단어
            dictionary[word]=idx
            idx+=1
            i-=1 # 이전단어부터 다시시작
            answer.append(dictionary[word[:-1]])
            word = ''
        i+=1

    if len(word)!=0: # 남은 단어가 있을경우
        answer.append(dictionary[word])

    return answer

msg ="TOBEORNOTTOBEORTOBEORNOT"
solution(msg)