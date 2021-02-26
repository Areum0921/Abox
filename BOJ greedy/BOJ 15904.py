S=input()
S_str=""
find_str=['U','C','P','C']
result=""
for i in S:
    if i.isupper(): #문장중에서 대문자만 저장
        S_str+=i

j=0
k=0
if(len(S_str)>0):
    while(1):#대문자들중에서 순서대로 UCPC가 나올수있는지 체크
        if S_str[j]==find_str[k]:
            result+=S_str[j]
            k+=1
        j+=1
        if(j>len(S_str)-1 or k>3):#문장끝까지 검사했거나, 이미 UCPC를 찾았거나
            break

if(result=="UCPC"):
    print("I love UCPC")
else:
    print("I hate UCPC")



