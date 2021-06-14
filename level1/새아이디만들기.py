from string import ascii_lowercase

def solution(new_id):
    cnt=0
    cnt2=0
    #step1
    new_id = new_id.lower()
    #step2
    new_id = new_id.strip()
    alpha_list=list(ascii_lowercase + "-" + "_" + ".")
    for i in range(0,10):
        alpha_list.append("%s"%i)
    new_id = ''.join(x for x in new_id if x in alpha_list)
    #step3
    while cnt != len(new_id):
        if new_id[cnt] == ".":
            cnt2 += 1
        else:
            if cnt2>1:
                new_id = new_id.replace("."*cnt2,".",1)
                cnt = 0
            cnt2 = 0
        if cnt == len(new_id) - 1 and new_id[cnt] == ".":
            new_id = new_id.replace("."*cnt2,".",1)
            break
        cnt += 1
    #step4
    if len(new_id) > 0:
        new_id = new_id.strip(".")
    #step5
    if len(new_id) == 0:
        new_id = "a"
    #step6
    if len(new_id) > 15:
        new_id = new_id[0:15]
        new_id = new_id.rstrip(".")
    #step7
    if len(new_id)<3:
        while len(new_id)<3:
            new_id = new_id + "%s"%new_id[-1]
    answer = new_id
    return answer
