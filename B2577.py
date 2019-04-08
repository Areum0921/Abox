T=int(input(""))
slist=[]

for i in range(T):
    answer=input("")
    score=0
    num=0
    for i in range(len(answer)):
        if(answer[i]=='O'):
            num=num+1
            score=score+num
        if(answer[i]=='X'):
            num=0
    slist.append(score)


for i in range(len(slist)):
    print(slist[i])
