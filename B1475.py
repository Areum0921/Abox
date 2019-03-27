import math
slist=[0,0,0,0,0,0,0,0,0] #0부터 8까지 카운트용 리스트

T=str(input(""))

for i in range(len(T)):
    ans=int(T[i])
    if(ans==9):#6과 9는 1세트당 2개까지 가능 ex)1세트 66,69,99,96
        ans=6
    slist[ans]=slist[ans]+1

slist[6]=math.ceil(slist[6]/2)#6과 9는 1세트당 2개까지 가능->반나눠서 2.5(총5개)일때 3세트필요
                            #0.5개는 반올림하여 한세트 더 추가
print(max(slist))#카운트된값중 가장 큰값만큼의 세트가 필요
