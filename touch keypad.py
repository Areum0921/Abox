def solution(numbers, hand):
    answer = ''
    l_state = [[3, 0]]
    # 왼손 초기 위치
    r_state=[[3, 2]]
    # 오른손 초기 위치

    for i in range(len(numbers)):
        print(numbers[i])
        distL = 0
        distR = 0
        print(l_state, r_state)
        if((numbers[i]==1 or numbers[i]==4 or numbers[i]==7)==True):

            answer+="L"
            l_state=[[numbers[i]//3, 0]] # 왼쪽일때 현재위치
            print(numbers[i] // 3, 0)
        elif((numbers[i]==3 or numbers[i]==6 or numbers[i]==9)==True):

            answer+="R"
            r_state=[[(numbers[i]//3-1), 2]] # 오른쪽일때 현재위치
            print(numbers[i] // 3 - 1, 2)
        elif((numbers[i]==2 or numbers[i]==5 or numbers[i]==8 or numbers[i]==0)):

            if(numbers[i]==0):
                distL = abs(l_state[0][0] - 3) + abs(l_state[0][1] - 1)
                distR = abs(r_state[0][0] - 3) + abs(r_state[0][1] - 1)
                print("num0","distl",distL,"distr",distR)
                if(distL>distR):# 오른손이 더 가까울때
                    r_state = [[3, 1]]
                    answer+="R"# 왼손이 더 가까울때
                elif(distL<distR):
                    l_state = [[3, 1]]
                    answer+="L"
                else:
                    if(hand=="right"):
                        r_state = [[3, 1]]
                        answer+="R"
                    else:
                        l_state = [[3, 1]]
                        answer+="L"
            else:

                distL = abs(l_state[0][0] - (numbers[i]//3)) + abs(l_state[0][1]-1)
                distR = abs(r_state[0][0] - (numbers[i]//3)) + abs(r_state[0][1]-1)

                if (distL > distR): # 오른손이 더 가까울때
                    r_state = [[numbers[i] // 3, 1]]
                    answer += "R"
                elif (distL < distR): # 왼손이 더 가까울때
                    l_state = [[numbers[i] // 3, 1]]
                    answer += "L"
                else:
                    if (hand == "right"):
                        r_state = [[numbers[i] // 3, 1]]
                        answer += "R"
                    else:
                        l_state = [[numbers[i] // 3, 1]]
                        answer += "L"
            print(numbers[i] // 3, 1)


    print(answer)
    return answer

numbers=[7, 0, 8, 2, 8, 3, 1, 5, 7, 6, 2]
hand="left"
solution(numbers, hand)