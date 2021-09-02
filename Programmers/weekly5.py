def solution(word):
    answer = 0
    val = [781,156,31,6,1] # 자리수 별 단어 개수
    # 첫번째자리에 E가 오면 첫번째 Exxxx는 782번째

    alpha = ['A','E','I','O','U']
    for i in range(len(word)):
        idx = alpha.index(word[i]) # 사전에서 몇번째 순서 알파벳인지
        answer += val[i]*idx+1 # 순서*자리수
    print(answer)
    return answer

word = 'U'
solution(word)