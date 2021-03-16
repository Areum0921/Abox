# str 타입의 숫자도 비교가능한 것을 모르고 뻘짓..
# "3" < "6" --> True
# "021" < "033" --> True
# "21" < "033" --> False , 자리수가 k+1보다 못하면 앞에 0채워준다.
k=int(input())
boo=input().split(" ")
check=[False]*10 # 0~9까지 중복없이 사용해서 조합 가능 체크.
max_num=""
min_num=""

def comp(i,j,k): # 부등호 넣고 비교하기
    if(k=='<'):
        return i < j
    elif(k=='>'):
        return i > j

    return True

def answer(cnt,s):
    global max_num, min_num
    if(cnt==k+1): # k+1개만큼 가능한 숫자 조합 만들었을때, 부등호 k개면 필요한 숫자가 k+1개
        if(not len(min_num)):
        # min_num이 비어있으면, 작은 수부터 차례로 조합을 만드는데 처음 만들수있는 조합이 제일 작은 수.
            min_num=s
        else: # 후에 만들 조합일수록 큰수 ex) 1 < 일때 (7<8) < (8<9)
            max_num=s
        return

    for i in range(10):
        if(check[i]==False):
            if(cnt==0 or comp(s[-1],str(i),boo[cnt-1])):
                check[i]=True
                answer(cnt+1,s+str(i)) # cnt 횟수1증가 및 부등호 연산에 적합하다면 s에 i 이어써주기
                check[i]=False

answer(0,"") # cnt 0부터, s=""부터 시작해서 조건에 맞을때마다 숫자 하나씩 이어써주기
print(max_num)
print(min_num)

