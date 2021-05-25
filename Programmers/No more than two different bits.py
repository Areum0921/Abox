# 비트가 0으로 끝나면 맨끝 비트를 1올려주면 된다. -> 이때, 차이나는 비트수는 1개며, 제일작은 숫자 조건에 만족하기때문
# 비트가 1로 끝나면 제일 작은 0을 찾고 다음 1과 위치 교환
# ex) 100111 일경우  3번째 0, 4번째가 1이다 이 둘을바꿔주면 101011 로 비트 1~2개차이내 가장 작은 숫자가 된다.
# 테스트 2번 케이스가 계속 실패했었음. -> 원인 : zfill 범위를 작게 줘서
# zfill 17부터 통과

def solution(numbers):
    answer = []

    for i in numbers:
        bin_num=bin(i)[2:].zfill(17)
        if bin_num[-1]=='0': # 맨 뒤 비트가 0일때
            #print(bin_num, bin(i+1)[2:].zfill(16),i,i+1)
            answer.append(i+1)
        else:
            first_zero=bin_num.rfind('0') # 제일 작은 0의 위치 인덱스 rfind 뒤에서부터 찾기 (오른쪽부터)
            bin_num=bin_num[:first_zero]+'10'+bin_num[first_zero+2:] # 찾아낸 0과 0보다 작은위치에 있는 1 위치교환
            #print(bin(i)[2:].zfill(16),bin_num,i,int(bin_num,2))
            answer.append(int(bin_num,2)) # 2진수를 10진수로 변환
            if(i>=int(bin_num,2)):
                print("i보다 작음")
    return answer

numbers=[i for i in range(300000)]
a=solution(numbers)


