def solution(num):
    answer = 0
    cnt=0
    while(1):
        if(num==1):
            answer+=cnt
            break
        elif(cnt>500):
            answer=-1
            break
        elif(num%2==0):
            num=num/2
        elif(num%2!=0):
            num=(num*3)+1
        print(num," ")
        cnt += 1
    print(answer)
    return answer

num=626331
solution(num)