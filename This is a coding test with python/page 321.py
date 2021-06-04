N=int(input())

N=str(N)

answer1=0
answer2=0

for i in range(len(N)//2):
    answer1+=int(N[i])
    answer2+=int(N[len(N)//2+i])
    print(N[i],N[len(N)//2+i])

if answer1==answer2:
    print("LUCKY")
else:
    print("READY")