def solution(seoul):
    answer = ''
    loc = seoul.index("Kim")

    answer+="김서방은 %d에 있다"%loc
    print(answer)
    return answer

seoul=["Park","Kim"]
solution(seoul)