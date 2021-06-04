S=input()
alpha=[]
number=0

for i in S:
    if ord(i)>=65: # 알파벳은 list로 (정렬을 위해)
        alpha.append(i)
    else:
        number+=int(i) # 숫자는 더해주기

alpha.sort()
print(''.join(map(str,alpha)) + str(number))