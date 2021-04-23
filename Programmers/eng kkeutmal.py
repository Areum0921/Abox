# 몇번째사람인지, 몇번째 단어인지 계속 안맞게 나와서 헤맸는데
# TC words만 수정해주고 n은 그대로 두고선 왜 다르게 나오지 했다..

def solution(n, words):
    answer = [0,0]
    data={}
    data[words[0]]=1

    for i in range(1, len(words)):
        if data.get(words[i]) or words[i - 1][-1] != words[i][0]:
            answer=[(i % n)+1,(i // n)+1]
            # print(i%n,"번째 사람", 2 + i//n)
            break
        else:
            data[words[i]] = 1

    return answer

n=2
words=["hello", "one", "even", "never", "now", "world", "draw"]
solution(n,words)