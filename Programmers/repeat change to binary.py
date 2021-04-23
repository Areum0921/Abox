def solution(s):
    answer = []
    total = 0
    i = 0
    while (len(s) > 1):
        binarys = s
        print(s)
        cnt = binarys.count('1')  # 1의 개수 세기
        cnt0 = len(binarys) - cnt  # 0의 개수
        i += 1  # 변환 횟수
        total += cnt0  # 0제거 횟수
        binarys = cnt * '1'  # 0제거후 1만 입력
        s = bin(len(binarys))[2:]  # 길이를 2진수로 변형

    answer.append(i)
    answer.append(total)
    print(answer)
    return answer

s="110010101001"
solution(s)