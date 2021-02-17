#input -> input을 sys.stdin.readline() 수정시
#108ms -> 104ms
import sys
N=int(sys.stdin.readline())
text_arr=[]
arry=[0]*26 #알파벳 위치 계산용. arry[0]은 A arry[25]는 Z (90-65, 90-65)
#대문자만 입력가능
sum=0
for i in range(N):
    text_arr.append(sys.stdin.readline())
#sys.stdin.readline()로 append이용시 맨뒤에\n도 같이 들어감
#ex) 아래와 같이 입력시
#2
#AA
#AA
#input의 경우 ["AA","AA"]
#sys.stdin.readline()의 경우 ["AA\n",'AA\n"]이된다.
for i in range(len(text_arr)):
    for j in range(len(text_arr[i])-1):
        arry[ord(text_arr[i][j])-65]+=int("1".ljust(len(text_arr[i])-j-1,"0"))



arry.sort(reverse=True)#sorting해서 앞에 10개까지만 계산해주기
for i in range(10):#숫자의 개수는 최대 10개
    sum+=int(arry[i])*(9-i)

print(arry)
print(sum)





