# 1 * (2, 3, 5) = 2, 3, 5
# (2, 3, 5) * (2, 3, 5) = 4, 6, 10, 6, 9, 15, 10, 15, 25
# (4, 6, 10, 6, 9, 15, 10, 15, 25) * (2, 3, 5)

N = int(input())

ugly=[0]*N
ugly[0]=1 # 첫번째 못생긴 수는 1

idx2, idx3, idx5 = 0,0,0

multiple2,multiple3,multiple5 = 2,3,5
print(multiple2,multiple3,multiple5)

for i in range(1,N):
    print("multiple",multiple2,multiple3,multiple5)
    ugly[i]=min(multiple2,multiple3,multiple5)
    print(ugly)
    if ugly[i]==multiple2:

        idx2 += 1
        multiple2 = ugly[idx2]*2
        print(i, ugly[i], "2의배수")
    if ugly[i] == multiple3:

        idx3 += 1
        multiple3 = ugly[idx3] * 3
        print(i, ugly[i], "3의배수")
    if ugly[i]==multiple5:

        idx5 += 1
        multiple5 = ugly[idx5]*5
        print(i, ugly[i], "5의배수")
print(ugly[N-1])





