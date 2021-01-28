def solution(arr):
    answer = []
    min_num=min(arr)
    del arr[arr.index(min_num)]
    if(len(arr)==0):
        answer.append(-1)
    else:
        answer=arr

    return answer

arr=[2,3,1,4]
solution(arr)