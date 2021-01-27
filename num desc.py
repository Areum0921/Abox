def solution(n):
    num = list(map(int, (str(n))))#int형 리스트
    num.sort(reverse=True) # 각숫자들을 역sort
    num2 = list(map(str, num))#역sort한 결과를 다시 str형태 리스트로

    answer = int("".join(num2))#문자열 리스트를 이어 int형으로 변환
    return answer


n=118732
solution(n)