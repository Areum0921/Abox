# 맨 앞숫자가 커야 제일 큰 숫자를 만들 수 있다.
#
def solution(number, k):
    answer=''
    num=[]
    num.append(number[0])
    for i in number[1:]:
        while(len(num)>0 and k>0 and num[-1]<i):
            # 기존에 담은 숫자보다 새로넣을수가 더 크면서
            # 제거가능한 숫자가 있을때 k!=0
            k-=1
            num.pop()#이전에 담은 숫자 제거
        #제거가능한 숫자가 없을경우나, 기존담은 숫자가 더 클 경우
        num.append(i)


    for j in range(len(num)-k):
        answer+=num[j]
    print(answer)
    return answer

number="9897"
k=2
solution(number,k)