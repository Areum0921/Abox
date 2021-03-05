#난쟁이는 총 9명, 진짜 난쟁이들의 키 합은 100
#9명의 키 합을 구해서 -100 하고 난 숫자를 2명의 난쟁이키로 조합해본다.
import sys
nanjang=[]
for i in range(9):
    n=int(sys.stdin.readline())
    nanjang.append(n)
nanjang.sort()
print(nanjang)
fake_nanjang=sum(nanjang)-100 # 가짜난장이들의 키 합
f1=0#첫번째 가짜난장이
f2=0#두번째 가짜난장이

i=0
while(1):
    if(fake_nanjang-nanjang[i] in nanjang):
        f1=fake_nanjang-nanjang[i]
        f2=nanjang[i]
        break
    i+=1

for i in nanjang:
    if(i!=f1 and i!=f2):
        print(i)


