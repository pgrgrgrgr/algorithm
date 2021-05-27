def solution(dartResult):
  answer = 0
  scorelist=[]
  strbin=['']*(len(dartResult)//2)
  cnt=0
  while True:
    for i in dartResult:
      if i not in '#,*':
        strbin[cnt] += i
      else:
        strbin[cnt] += i
        cnt += 1
    break
  for i in range(len(strbin)):
    for j in range(len(strbin[i])):
      if '10' in strbin[i]:
        if strbin[i][j] in 'S,D,T':
          if strbin[i][j] == 'S':
            scorelist.append(strbin[i][j-1])
          elif strbin[i][j] == 'D':
            scorelist.append(int(strbin[i][j-1])**2)
          elif strbin[i][j] == 'T':
            scorelist.append(int(strbin[i][j-1])**3)
        elif strbin[i][j] in '#,*':
          scorelist.append(strbin[i][j]) 
  print(strbin)
  print(scorelist)
  for i in range(len(scorelist)):
    if scorelist[i] == '#'or'*':
      if scorelist[i] == '*':
        if i>1:
          scorelist[i-2] = scorelist[i-2] * 2
          scorelist[i-1] = scorelist[i-1] * 2
        else:
          scorelist[i-1] = scorelist[i-1] * 2
      elif scorelist[i] == '#':
        scorelist[i-1] = int(scorelist[i-1]) * (-1)
  print(scorelist)
  for i in scorelist:
    if not str(i).isdigit():
      scorelist.remove(i)
  answer = sum(scorelist)
  print(answer)

          
  return answer
solution("1D2S#10S")
