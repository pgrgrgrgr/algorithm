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
    return answer
