a=input().split('-') # - 기준으로 나누기
sum=0

for i in a[0].split('+'): # a[0]은 양수, 식을 계산해 더해주기
    sum+=int(i)

for i in a[1:]:
    for j in i.split('+'): #-기준으로 쪼갠 결과들을 연산하여 첫값에서 다 빼주기
        sum-=int(j)

print(sum)



