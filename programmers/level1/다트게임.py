import re

def solution(dartResult):
  answer = 0
  scorelist1=[]
  sorteddR = re.findall(r'\d+\w\*|\d+\w\#|\d+\w',dartResult)
  for i in range(len(sorteddR)):
      while True:
        if len(sorteddR[i]) == 3:
          if sorteddR[i][-1] == "S":
            scorelist1.append(10 ** 1)
          if sorteddR[i][-1] == "D":
            scorelist1.append(10 ** 2)
          if sorteddR[i][-1] == "T":
            scorelist1.append(10 ** 3)
        elif len(sorteddR[i]) == 2:
          if sorteddR[i][-1] == "S":
            scorelist1.append(int(sorteddR[i][0]) ** 1)
          if sorteddR[i][-1] == "D":
            scorelist1.append(int(sorteddR[i][0]) ** 2)
          if sorteddR[i][-1] == "T":
            scorelist1.append(int(sorteddR[i][0]) ** 3)
        
        if sorteddR[i][-1] == "*":
          if sorteddR[i][-2] == "S":
            scorelist1.append("%d*"%(int(sorteddR[i][0]) ** 1))
          if sorteddR[i][-2] == "D":
            scorelist1.append("%d*"%(int(sorteddR[i][0]) ** 2))
          if sorteddR[i][-2] == "T":
            scorelist1.append("%d*"%(int(sorteddR[i][0]) ** 3))
        if sorteddR[i][-1] == "#":
          if sorteddR[i][-2] == "S":
            scorelist1.append(int(sorteddR[i][0]) ** 1 * (-1))
          if sorteddR[i][-2] == "D":
            scorelist1.append(int(sorteddR[i][0]) ** 2 * (-1))
          if sorteddR[i][-2] == "T":
            scorelist1.append(int(sorteddR[i][0]) ** 3 * (-1))
        break

  for i in range(len(scorelist1)):
    if type(scorelist1[i]) == str:
      if scorelist1[i][-1] == "*" and i == 0:
        scorelist1[i] = int(scorelist1[i].rstrip("*")) * 2
      elif scorelist1[i][-1] == "*" and i>0:
        scorelist1[i-1] = scorelist1[i-1] * 2
        scorelist1[i] = int(scorelist1[i].rstrip("*")) * 2
        
  answer = sum(scorelist1)
  return answer
