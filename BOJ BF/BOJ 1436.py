# '666'이 한개만 있을때로 하다가 계속 틀렸다. 666666의 경우 666이 2개지만, 조건에 부합함.
# 문제를 다시보니 6이 적어도 3개이상 연속으로 들어가는 수였다.
number='666'
i=1
cnt=1
N=int(input())
if(N>1):
    while(1):
            number=str(int(number)+i)
            if(number.count('666')>0):
                # 6개 3개이상연속인게 1개이상 존재할때
                cnt+=1
            if(cnt==N):
                break
else:
    number='666'
print(number)