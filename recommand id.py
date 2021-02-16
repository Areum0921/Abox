def solution(new_id):
    answer = ''
    check = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j',
             'k', 'l', 'n', 'm', 'o', 'p', 'q', 'r', 's', 't',
             'u', 'v', 'w', 'x', 'y', 'z', '1', '2', '3', '4',
             '5', '6', '7', '8', '9', '0', "-", "_", "."]
    new_id = new_id.lower()  # 1단계
    check_str = ''
    check_str2 = ''
    check_dot = ''

    for i in range(len(new_id)):  # 2단계 가능한문자 체크
        if (new_id[i] in check):
            check_str = check_str + new_id[i]

    check_str += ' '
    for i in range(len(check_str) - 1):  # 3단계 마침표 중복 제거
        if (check_str[i] == '.' and check_str[i + 1] == '.'):
            check_str2 += ''
        else:
            check_str2 += check_str[i]

    if (len(check_str2) > 0):  # 4단계
        for i in range(len(check_str2)):  # 맨 앞, 맨뒤 . 제거

            if (i == 0 and check_str2[0] == '.'):
                check_dot += ''
            elif (i == len(check_str2) - 1 and check_str2[i] == '.'):
                check_dot += ''
            else:
                check_dot += check_str2[i]
    answer = check_dot

    if (len(check_dot) == 0):  # 5단계 빈 문자열일때 new_id에 a대입
        check_dot += 'a'

    if (len(check_dot) > 15):  # 6단계 16글자 이상일때

        check_dot = check_dot[0:15]

        if (check_dot[-1] == '.'):
            check_dot = check_dot[0:14]
        answer = check_dot
    if (len(check_dot) <= 2):  # 7단계 아이디가 2글자 이하일때

        if (len(check_dot) == 1):
            check_dot += check_dot[-1]
            check_dot += check_dot[-1]
        elif (len(check_dot) == 2):
            check_dot += check_dot[-1]
        answer = check_dot

    return answer