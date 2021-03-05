import sys

x=1000000
era=[0]*(x+1)

for i in range(2, int(x**0.5)+1): #먼저 100만까지 소수 만들어놓기, 제곱근까지만 돌려도된다.
    if(era[i]==0): #era[i]의 값이 소수여도, i의 배수들은 소수가 아니다.
        for j in range(i+i,x+1 ,i):#i가 2일때, 4,6,8 등은 소수가 될수없다.
            era[j]=1 # 소수가 아닌숫자들은 1로 변경해준다
'''
prime=[]
for i in range(2,len(era)):
    if(era[i]!=1):
        prime.append(i) # 100만이하 소수 숫자들
print(len(prime))
'''
#era[인덱스값]=0 이면 소수임을 활용하자.
#era[17]=0이면 17이 소수라는뜻.
def goldbach(n):
    i=2
    while(1):
        if(n-i<=0):# n 이하의 수에서 소수값의 조합을 찾는데, i가 n보다 커지면 없다는뜻이다.
            print("Goldbach's conjecture is wrong.")
            break
        if(era[i]==0 and era[n-i]==0):# n이 20일때 i가 3이고 소수면서, 20-3=17이 소수면 골드바흐 추측이 성립한다.
            print(n,"=",i,"+",n-i)
            break
        i+=1
#while문안에 in을 써서 그런지 시간초과난다. prime 숫자들을 굳이 따로 쓰지않고 era배열을 써야할듯싶다.
    '''
    while(1):
        if(n-num1 in prime):
            num2=n-num1
            print(num1 + num2, '=', num1, '+', num2)
            break
        else:
            r+=1
            num1=prime[r]
        if(prime[r]>=n):
            print("Goldbach's conjecture is wrong.")
            break
    '''
# 모든 소수쌍을 시도하면 시간초과난다
''' 
    while(num1+num2!=n): # 제일 작은수, 제일 큰수 부터 더해준다
        if(num1+num2>n): # 더한값이 n보다 크면 num2를 그 다음번째 큰수로 변경
            l-=1
            num2=gold_prime[l]
        if(num1+num2<n):# 더한값이 n보다 작으면 num1을 현재 num1다음 수로 변경
            r+=1
            num1=gold_prime[r]
        if(r>len(gold_prime)//2 and l<len(gold_prime)//2):# 못구하면
            break
    if(num1+num2==n):
        print(num1+num2,'=',num1,'+',num2)
    else:
        print("Goldbach's conjecture is wrong.")
'''

while(1):
    n=int(sys.stdin.readline())
    if (n == 0):
        break
    goldbach(n)





