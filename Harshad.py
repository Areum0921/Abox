def solution(arr):
    answer = True
    str_arr=str(arr)
    num1=0
    for i in range(len(str_arr)):
        num1+=int(str_arr[i])

    if(arr%num1!=0):
        answer = False

    return answer
arr=10
solution(arr)