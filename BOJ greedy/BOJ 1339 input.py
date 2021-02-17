N=int(input())
text_arr=[]
arry=[0]*26 #알파벳 위치 계산용. arry[0]은 A arry[25]는 Z (90-65, 90-65)
#대문자만 입력가능
sum=0
for i in range(N):
    text_arr.append(input())

for i in range(len(text_arr)):
    for j in range(len(text_arr[i])):
        arry[ord(text_arr[i][j])-65]+=int("1".ljust(len(text_arr[i])-j,"0"))


arry.sort(reverse=True)#sorting해서 앞에 10개까지만 계산해주기
for i in range(10):#숫자의 개수는 최대 10개
    sum+=int(arry[i])*(9-i)

print(sum)





