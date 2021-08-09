def solution(s):
  answer = []
  s = s.lstrip("{")
  s = s.rstrip("}")
  s = s.split("},{")
  s = sorted(s,key=lambda x:len(x))
  for i in s:
    tmp = i.split(',')
    for j in tmp:
      if int(j) not in answer:
        answer.append(int(j))
    
  return answer