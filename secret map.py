#bin(a) : a를 이진수로 나타낸다
#bin(a|b) : a와 b를 이진수로 나타내고 or로 겹쳐?준다
#a.rjust(number) : a의 길이가 number보다 짧을때 number길이만큼 오른쪽부터 공백으로 채워준다
#a.ljust(number) : rjust와 반대로 왼쪽부터 공백 채워준다
def solution(n,arr1,arr2):
    arr1_binary=[]
    arr2_binary=[]
    answer=[""] * n

    for i in range(n): # arr1, arr2 이진수 생성
        arr1_binary.append(make_binary(n,arr1[i]))
        arr2_binary.append(make_binary(n,arr2[i]))

    for j in range(n): # 두 arr를 겹친 이진수
        for k in range(n):
            if(arr1_binary[j][k]+arr2_binary[j][k]!=0):
                answer[j]+="#"
            else:
                answer[j]+=" "
    print(arr1_binary,"\n", arr2_binary,"\n",answer)


def make_binary(n,num): #이진수 만들기
    binary=[]
    while(1):
        a=num%2
        b=num//2
        if(num==0):
            break
        else:
            binary.append(a)
            num=b
    binary.reverse()
    while (len(binary) != n):  # 2진수결과값이 n자리 미만일때 앞에 0채워주기
        binary.insert(0, 0)

    return binary

n=6
arr1=[46,33,33,22,31,50]
arr2=[27,56,19,14,14,10]
solution(n,arr1,arr2)


