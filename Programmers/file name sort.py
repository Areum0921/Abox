import re
def solution(files):
    answer = []
    split_result = []
    for i in files:
        split_result.append(re.split("(\d+)", i))  # 숫자 기준으로 앞 , 숫자, 뒤 쪼개기
        print(split_result)
    split_result = sorted(split_result, key=lambda x: (x[0].lower(), int(x[1])))  # 앞 문자열 lower로 통일시켜 정렬,
    # x[1]은 int로 0001 == 1 등, 0이붙은 숫자도 같은 수로 인식
    for i in split_result:
        answer.append(''.join(i))

    print(answer)
    return answer

"""
같은 방식인데 아래 코드는 실패
1. 찾아낸 원인 : 파일 확장자 부분에도 숫자가 들어갈 수 있음. 그래서 (\d+)로 처음 나오는 숫자 앞, 뒤로 쪼갰어야함
ex) 이방식대로라면 "F-0004.png45" 일때, F-, 0004, .png, 45 이렇게 쪼개져버린다.
ex) F-4.pn233g233 일때 F-, 4, .pn, 233, g, 233으로 쪼개짐
# 숫자 부분을 따로 처리해주면 되긴 하겠지만 복잡해질듯

    def solution(files):
    answer = []
    split_result = [[] for _ in range(len(files))]

    for i in range(len(files)):
        str_part=re.findall("\D+",files[i]) # 문자 부분만 뽑아내기
        int_part=re.findall("\d+",files[i])

        split_result[i].append(str_part[0]) # HEAD
        split_result[i].append(int_part[0]) # NUMBER
        if len(str_part)>1:
            split_result[i].append(str_part[1]) # TAIL
        else:
            split_result[i].append("")
        print(split_result)


    split_result = sorted(split_result,key=lambda x : (x[0].lower(),int(x[1]))) # 정렬 기준 HEAD, NUMBER 순

    for i in split_result:
        answer.append(''.join(i))

    print(answer)
    return answer
"""


files= ["F-15","F-00004.png","F-04 freedom Fighter.jpg","F-0004.png",]
solution(files)