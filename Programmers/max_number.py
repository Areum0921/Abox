def solution(numbers):
    str_numbers = [] # 문자열로 바꾼 numbers
    for i in range(len(numbers)):  # 문자열로 바꾸기
        str_numbers.append(str(numbers[i]))

    str_numbers.sort(key=lambda x: x * 4, reverse=True)  # numbers의 원소는 1000이하 최대 4자리
    # ex) 101,102,13일때
    # 101101101101 , 102102102102, 13131313 으로 비교
    # 맨앞자리는 다 1 -> 다음자리 검사
    # 2번째자리 0,0,3 -> 13먼저
    # 3번째자리 1,2 -> 102
    # 101
    # 이런식으로 순서를 정하게된다.

    # 11번만 자꾸틀림 -> 0만 입력됐을때를 생각해야함 [0,0,0,0] -> 0
    answer = str(int(''.join(str_numbers)))
    # 0000을 int로 변환해주면 0이된다.
    print(answer)
    return answer

numbers=[0,0,0,0,0]
solution(numbers)