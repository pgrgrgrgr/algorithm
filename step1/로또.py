def solution(lottos, win_nums):
    answer = []
    count=0
    count2=0
    while lottos:
        for i in lottos:
            if i in win_nums:
                lottos.remove(i)
                count+=1
            if i not in win_nums and i != 0:
                lottos.remove(i)
            if i == 0:
                lottos.remove(i)
                count2+=1
    answer.append(7-(count+count2) if count+count2 > 0 else 6)
    answer.append(7-count if count>0 else 6)
    
    return answer