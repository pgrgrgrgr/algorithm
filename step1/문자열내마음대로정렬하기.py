def solution(strings, n):
  answer = []
  dic1={}

  for i in range(len(strings)):
    dic1[strings[i]] = strings[i][n]
  
  dic1 = sorted(dic1.items(),key=lambda x:x[0])
  dic1 = sorted(dic1, key = lambda x:x[1])
  
  for i,j in dic1:
    answer.append(i)

  return answer

# def solution(strings, n):
#   answer = []
#   answer = sorted(answer,key=lambda x:x[n])
#   return answer
# ㅇㄴ..