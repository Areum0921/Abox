def solution(n):
    answer = 0

    arr=[]
    while(1):

        num1=n%3
        n=n//3
        arr.append(num1)
        if(n==0):
            break

    for i in range(len(arr)-1,-1,-1):
        #print(i,arr[-i+len(arr)-1])
        if(i>0):
            #print(3 ** i * arr[-i+len(arr)-1])
            answer+=3**i*arr[-i+len(arr)-1]
        elif(i==0):
            #print(3 ** i * arr[-i+len(arr)-1])
            answer+=3** i * arr[-i+len(arr)-1]

    return answer

solution(45)
