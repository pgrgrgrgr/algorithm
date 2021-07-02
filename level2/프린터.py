def solution(priorities, location):
  answer = 0
  print_dic = {}
  
  for i in range(len(priorities)):
    print_dic[i] = priorities[i]
  cnt = 0
  while priorities:
    sliced_tmp = priorities[cnt + priorities.index(max(priorities)):-1]

  return answer

solution([2,1,3,2],2)