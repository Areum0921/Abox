from itertools import permutations

def check(user,banned_id): # 확인
    for i in range(len(banned_id)): # 각 banned_id에는 1명의 유저씩 가능
        if len(user[i])!=len(banned_id[i]):
            return False

        for j in range(len(banned_id[i])):
            if banned_id[i][j] == '*': # 넘어가기
                continue
            if banned_id[i][j] != user[i][j]: # '*'가 아님에도 같은문자가 아니면 해당유저는 ban아님
                return False

    return True

def solution(user_id, banned_id):
    answer = []
    user_per = list(permutations(user_id,len(banned_id))) # user_id에서 ban된 id개수씩 만들수있는 가능한 모든 순열

    for user in user_per:
        if check(user,banned_id)==False: # 현재 순열 user랑 banned_id로 가능한 경우가 아닐때
            continue
        else:
            user=set(user) # set으로 형태변환 후 answer dict에 없으면 해당 순열 추가
            if user not in answer:
                answer.append(user)
    print("ans",answer)



user_id = ["frodo", "fradi", "crodo", "abc123", "frodoc"]
banned_id = ["fr*d*", "*rodo", "******", "******"]
solution(user_id,banned_id)