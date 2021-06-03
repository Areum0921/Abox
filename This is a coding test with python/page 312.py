# 1자리씩 x or + 연산
# 필요한 연산의 수 = len(S)-1
# 0,1을 제외하고 곱해주는 것이 제일 큰 수가 나온다.
# 1의경우 곱하면 그대로지만, 더해주면 1 더커짐.
S=input()
need=len(S)-1 # 필요한 연산의 수
answer=0

for i in S:
    num=int(i)
    if num>1 and answer>0:
        answer*=num
    else:
        answer+=num

print(answer)





