def solution(arr1, arr2):
    answer = [[0] * len(arr1[0]) for _ in range(len(arr1))]

    for i in range(len(arr1)):
        for j in range(len(arr1[0])):
            answer[i][j]=arr1[i][j]+arr2[i][j]


    print(answer)
    return answer

arr1=[[1,2,3]]
arr2=[[2,3,4]]
solution(arr1, arr2)