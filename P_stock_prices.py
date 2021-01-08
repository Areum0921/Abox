def solution(prices):
    answer = []
    
    j=0
    for i in (prices):
        k=0
        count=0
        while(1):
            if(k+j>=len(prices)):
                break
            elif(i<=prices[k+j]):
                count=count+1
            elif(i>prices[k+j]):
                count=count+1
                break
            k=k+1
        j=j+1
        answer.append(count-1)

    return answer

prices=[1,2,3,2,3,3,1]

solution(prices)
