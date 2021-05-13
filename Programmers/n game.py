# 1~n까지 각 진수로 변환해 str로 쭉 이어붙인다
# 튜브순서에 해당하는 문자열만 저장
# 최대 나중까지 말해야하는 경우 : 16진수, 100명일때, 100번째순서에, 1000개의 숫자를 구할때 = 10만번째
# 진법은 2,8,16 뿐만아니라 2,3,4,5,6,7,8,... 16진법이다.

def change(n,num): # num을 n진수로 변환 -> num // n + num % n
    arr='0123456789ABCDEF' # 최대 16진수
    res=''
    if num==0:
        return '0'
    while num > 0:
        res = arr[num%n] + res # num%n을 앞에 붙여나가는식
        num = num//n # num을 n으로 나눈후 나머지를 앞에 붙여주기 반복
    #print(res)
    return res

def solution(n, t, m, p):
    answer = ''
    result = ''
    turn = []
    turn.append(p)
    for i in range(t - 1):  # 튜브가 말해야하는 턴
        turn.append(turn[-1] + m)

    for i in range(t*m):
        result+=change(n,i) # i를 n진수로 변환해 result에 저장

    # print(turn)
    # print(result)

    for i in turn:  # 나열된 순서중에서 튜브턴만 뽑아내기
            answer += result[i - 1] # 1번째순서는 0번인덱스부터
    #print(answer,len(answer))

    return answer

solution(16,1000,100,100)