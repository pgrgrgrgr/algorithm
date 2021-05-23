def solution(array, commands):
    new_array=[]
    answer = []
    for i in range(0,len(commands)):
        if commands[i][0]==commands[i][1]:
            new_array.append(array[commands[i][0]-1])
            answer.append(array[commands[i][0]-1])
        else:
            new_array.append(array[commands[i][0]-1:commands[i][1]])
            new_array[i].sort()
            answer.append(new_array[i][commands[i][2]-1])
    print(new_array)
    print(answer)

    return answer

solution([1],[[2,5,1],[4,4,1],[1,7,1]])