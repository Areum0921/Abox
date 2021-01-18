def solution(array, commands):
    answer = []

    for i in range(len(commands)):
        arr=[]
        num1 = commands[i][0]
        num2 = commands[i][1]

        for j in range(num1-1, num2):
            arr.append(array[j])

        arr.sort()
        print(arr)
        answer.append(arr[commands[i][2]-1])

    return answer

array = [1, 5, 2, 6, 3, 7, 4]
commands = [[2, 5, 3], [4, 4, 1], [1, 7, 3]]
solution(array, commands)