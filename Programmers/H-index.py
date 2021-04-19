def solution(citations):
    answer = 0
    cit_sort = sorted(citations, reverse=True)
    # 인용횟수 많은 순
    for i in range(len(cit_sort)):
        if (i + 1 <= cit_sort[i]):
            # 3,0,6,1,5 -> 6,5,3,1,0
            # 제일 많이 인용된 논문이 1번이상 ? 6번 yes answer=1
            # 2번째로 많이 인용된 논문이 2번이상 ? 5번 yes, 2번 인용된 논문수 2개 answer=2
            # 3번째로 많이 인용된 논문이 3번이상 ? 3번 yes, 3번 인용된 논문수 3개 answer=3
            # 4번째로 많이 인용된 논문이 4번이상 ? 1번 no. h값 = 3 answer=3 break
            answer = i + 1
    print(answer)
    return answer