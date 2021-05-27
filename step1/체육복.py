def solution(n, lost, reserve):
    binlist=[]
    lostset = set(lost)
    reserveset = set(reserve)
    lost = list(lostset-reserveset)
    reserve = list(reserveset-lostset)
    while len(lost)>0:
        bin = lost.pop()
        if (bin + 1) in reserve:
            reserve.remove(bin + 1)
        elif (bin - 1) in reserve:
            reserve.remove(bin - 1)
        else:
            binlist.append(bin)
    answer = n - len(binlist)
    return answer
