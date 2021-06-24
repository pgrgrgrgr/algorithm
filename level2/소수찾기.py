from itertools import permutations
import math

def solution(numbers):
  cnt=0
  answer = 0
  temp=''
  templist = []
  templist2 = []
  templist3 = []

  for i in range(1,len(numbers)+1):
    templist.append(set(permutations(numbers,i)))
  
  for i in templist:
    for j in i:
      for k in j:
        temp += k
      templist2.append(temp)
      temp=''

  for i in templist2:
    if i[0] == '0':
      continue
    else:
      templist3.append(i)
      
  for i in templist3:
    for j in range(2,int(math.sqrt(int(i))+1)):
      if int(i)%j == 0:
        cnt += 1
    if cnt == 0:
      answer += 1
    cnt = 0
    if i == '1':
      answer -= 1
      
  return answer

solution('0293')