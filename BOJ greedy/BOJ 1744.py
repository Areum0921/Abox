N=int(input())
arry_neg=[]
arry_pos=[]
sum=0
sum_state=0

for i in range(N): #음수 양수 나눠서 구하기
    num=int(input())
    if(num>1):#1의경우 더해주는게 더 큼. ex)1 2 일때 1+2=3 , 1*2=2
        arry_pos.append(num)
    elif(num<=0):#음수 x 0 = 0
        arry_neg.append(num)
    else:
        sum+=num

arry_pos.sort(reverse=True)
arry_neg.sort()

state=False

for n in arry_neg: #- * -는 양수이므로 절대값이 큰 순서대로 짝지어 곱해주기
    #print(n, sum_state,sum)
    if(state==False):
        sum_state=n
        sum+=sum_state
        state=True
    else:
        sum-=sum_state
        sum_state*=n
        sum+=sum_state
        sum_state=0
        state=False

state=False

for k in arry_pos: #큰 순서대로 짝지어 곱하기
    if (state == False):
        sum_state = k
        sum += sum_state
        state = True
    else:
        sum -= sum_state
        sum_state *= k
        sum += sum_state
        sum_state = 0
        state = False

print(arry_pos,arry_neg,sum)