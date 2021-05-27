# A와 B의값을 k번 바꿔 A배열의 합이 최대가 되도록 한다.
# A의 가장 작은값과, B의 가장 큰값을 바꾼다.
def change(A,B,k):

   A=sorted(A)
   B=sorted(B,reverse=True)
   # A는 오름차순, B는 내림차순
   # 각 인덱스에 해당하는 숫자끼리 바꿔주면된다.

   for i in range(k):
       if A[i]<B[i]:
        A[i],B[i]=B[i],A[i]
       else: # B[i]보다 A[i]가 더 크면, 앞으로도 마찬가지 for문을 멈춘다.
           break
   print(sum(A))

A=[1,2,9,8,7]
B=[5,5,6,6,5]
k=3
change(A,B,k)