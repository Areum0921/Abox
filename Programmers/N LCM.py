# arr중 가장큰값부터 시작해서(최소공배수기 때문에) arr안의 숫자로 모두 나눠지는 첫번째 수
def solution(arr):
    answer = 0
    k=max(arr)
    cnt = 0
    while(1):
        print(cnt)

        for i in arr:
            print(i,k, i%k)
            if(k%i==0):
                cnt+=1
            else:
                cnt = 0
                break
        if (cnt == len(arr)):
            answer = k
            break
        k += 1

    print(answer)
    return answer

arr=[2,6,8,14]
solution(arr)