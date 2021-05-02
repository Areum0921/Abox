# 2 3 2     5 4 3
# 4 2 4     2 4 1
# 3 1 4     3 1 1
# 행렬곱셈.
# 2 * 5 + 3 * 2 + 2 * 3 , 2 * 4 + 3 * 4 + 2 * 1 , 2 * 3 + 3 * 1 + 2 * 1
# 22 , 22 , 11

# n*m 행렬 * m*k 행렬의 곱셈 결과 크기 행렬은 n*k
def solution(arr1, arr2):
    answer = [[0 for _ in range(len(arr2[0]))] for _ in range(len(arr1))]

    for i in range(len(arr1)):
        for j in range(len(arr2[0])):
            for k in range(len(arr1[0])):
                print(i, j, "??", j, k,arr1[j][k],arr2[k][j])
                answer[i][j]+=arr1[i][k] * arr2[k][j]

    print(answer)
    return answer


arr1=[[2, 3, 2], [4, 2, 4], [3, 1, 4]]
arr2=[[5, 4, 3], [2, 4, 1], [3, 1, 1]]
solution(arr1,arr2)