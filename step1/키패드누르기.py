import math

def solution(numbers, hand):
    answer = ''
    numdic={}
    numdic[1] = [0,3]
    numdic[2] = [1,3]
    numdic[3] = [2,3]
    numdic[4] = [0,2]
    numdic[5] = [1,2]
    numdic[6] = [2,2]
    numdic[7] = [0,1]
    numdic[8] = [1,1]
    numdic[9] = [2,1]
    numdic["*"] = [0,0]
    numdic[0] = [1,0]
    numdic["#"] = [2,0]

    leftpoint = numdic["*"]
    rightpoint = numdic["#"]
    while numbers:
        if numbers[0] == 1:
            leftpoint = numdic[1]
            answer = answer + "L"
            numbers.remove(numbers[0])
        elif numbers[0] == 2:
            disfromleft = abs(numdic[2][0]-leftpoint[0]) + abs(numdic[2][1]-leftpoint[1])
            disfromright = abs(numdic[2][0]-rightpoint[0]) + abs(numdic[2][1]-rightpoint[1])
            if(disfromleft>disfromright):
                rightpoint = numdic[2]
                answer = answer + "R"
                numbers.remove(numbers[0])
            elif(disfromright>disfromleft):
                leftpoint = numdic[2]
                answer = answer + "L"
                numbers.remove(numbers[0])
            else:
                if hand=="right":
                    rightpoint = numdic[2]
                    answer = answer + "R"
                    numbers.remove(numbers[0])
                else:
                    leftpoint = numdic[2]
                    answer = answer + "L"
                    numbers.remove(numbers[0])
        elif numbers[0] == 3:
            rightpoint = numdic[3]
            answer = answer + "R"
            numbers.remove(numbers[0])
        elif numbers[0] == 4:
            leftpoint = numdic[4]
            answer = answer + "L"
            numbers.remove(numbers[0])
        elif numbers[0] == 5:
            disfromleft = abs(numdic[5][0]-leftpoint[0]) + abs(numdic[5][1]-leftpoint[1])
            disfromright = abs(numdic[5][0]-rightpoint[0]) + abs(numdic[5][1]-rightpoint[1])
            if(disfromleft>disfromright):
                rightpoint = numdic[5]
                answer = answer + "R"
                numbers.remove(numbers[0])
            elif(disfromright>disfromleft):
                leftpoint = numdic[5]
                answer = answer + "L"
                numbers.remove(numbers[0])
            else:
                if hand=="right":
                    rightpoint = numdic[5]
                    answer = answer + "R"
                    numbers.remove(numbers[0])
                else:
                    leftpoint = numdic[5]
                    answer = answer + "L"
                    numbers.remove(numbers[0])
        elif numbers[0] == 6:
            rightpoint = numdic[6]
            answer = answer + "R"
            numbers.remove(numbers[0])
        elif numbers[0] == 7:
            leftpoint = numdic[7]
            answer = answer + "L"
            numbers.remove(numbers[0])
        elif numbers[0] == 8:
            disfromleft = abs(numdic[8][0]-leftpoint[0]) + abs(numdic[8][1]-leftpoint[1])
            disfromright = abs(numdic[8][0]-rightpoint[0]) + abs(numdic[8][1]-rightpoint[1])
            if(disfromleft>disfromright):
                rightpoint = numdic[8]
                answer = answer + "R"
                numbers.remove(numbers[0])
            elif(disfromright>disfromleft):
                leftpoint = numdic[8]
                answer = answer + "L"
                numbers.remove(numbers[0])
            else:
                if hand=="right":
                    rightpoint = numdic[8]
                    answer = answer + "R"
                    numbers.remove(numbers[0])
                else:
                    leftpoint = numdic[8]
                    answer = answer + "L"
                    numbers.remove(numbers[0])
        elif numbers[0] == 9:
            rightpoint = numdic[9]
            answer = answer + "R"
            numbers.remove(numbers[0])
        elif numbers[0] == 0:
            disfromleft = abs(numdic[0][0]-leftpoint[0]) + abs(numdic[0][1]-leftpoint[1])
            disfromright = abs(numdic[0][0]-rightpoint[0]) + abs(numdic[0][1]-rightpoint[1])
            if(disfromleft>disfromright):
                rightpoint = numdic[0]
                answer = answer + "R"
                numbers.remove(numbers[0])
            elif(disfromright>disfromleft):
                leftpoint = numdic[0]
                answer = answer + "L"
                numbers.remove(numbers[0])
            else:
                if hand=="right":
                    rightpoint = numdic[0]
                    answer = answer + "R"
                    numbers.remove(numbers[0])
                else:
                    leftpoint = numdic[0]
                    answer = answer + "L"
                    numbers.remove(numbers[0])
    return answer
