# 17427문제와 같음
# 그대로 내면 시간초과, 입력받는 방식을 개선
# 입력받고 -> 계산 보다 입력을 먼저 다받고 계산시 (n log n) 그래도 시간 초과난다.
# x의 절반이상인 숫자들은 1번씩 나오므로 단순 더하기 --> 그래도 시간초과남
# 1~1000000까지 답을 넣어놓고 꺼내오는방식으로 해보기.
# 효율성 매우 중요.

x=1000000
arr = [0]*(x+2)
answer=0
arr2=[0]*(x+2)
for i in range(1,x+1): #f(a)구하기
    for j in range(1, ((x+1)//i)+1):
        arr[i*j]+=i
        # x이하의 수에서 i의 배수값들에 i를 더해준다.
        #ex) 10이하의 수에서 i가 5일때 j는 1부터 (10+1//5)+1 인 2까지.
        #arr[5*1]+=i, arr[5*2]+=i 이런식으로 더해준다.
        #i가 2일때 j는 1부터 (10+1//2)+1인 6까지
        #arr[2*1],[2*2],[2*3],[2*4],[2*5],[2*6] 를 +i씩
print("f(a)계산완료")
arr2[1]=arr[1]
for i in range(3,x+2): # g(n)구하기
    arr2[i-1]=arr[i-1]+arr2[i-2]
arr2.pop()
print("g(n)계산완료")

N=int(input())
num=[]
for i in range(N):
    num.append(int(input()))

for i in num:
    print(arr2[i])


'''
        if((x-(x//2))%2==0): # x의 절반이상숫자가 짝수개일때
            if(x%2==0):#x가 짝수일때
                answer2+=((x//2+1)+x) * ((x-(x//2))//2)
            else:
                answer2 += ((x // 2 + 1) + x) * ((x - (x // 2)) // 2)

        else:#x가 홀수일때

            if(x%2==0): #x가 짝수일때
                answer2 +=((x//2+1)+x) * ((x-(x//2))//2) + (((x//2+1)+x)//2)
            else:#x가 홀수일때
                answer2 += ((x // 2 + 1) + x) * ((x - (x // 2)) // 2) + (((x // 2 + 1) + x) // 2)
'''

