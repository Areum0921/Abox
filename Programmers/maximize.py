# 정규식 사용
from itertools import permutations
import re

def solution(expression):
    answer = 0
    op = set(re.findall("\D", expression))  # 기호만 뽑아내기
    print(op)
    op_list = permutations(op)  # 뽑아낸 기호들의 조합

    for i in op_list:
        tmp = re.compile("(\D)").split("" + expression) # complie = 정규식 객체 리턴
        # expression에서 기호를 문자열로 취급해 문자열 기준으로 쪼개기
        for j in i:
            while j in tmp:  # 기호가 있는동안 반복
                idx = tmp.index(j)  # 기호가 있는 위치
                tmp = tmp[:idx - 1] + [str(eval(''.join(tmp[idx - 1:idx + 2])))] + tmp[idx + 2:]
                # 기호 전전 인덱스 까지 + 기호 앞,뒤 인덱스포함 eval + 기호 뒤뒤 인덱스부터
                # 수식을 연산한 결과로 저장함 --> 즉, 가중치 순서에따라 연산

        if (answer < abs(int(tmp[0]))):  # 현재값보다 더 크면 갱신
            answer = abs(int(tmp[0]))

    return answer