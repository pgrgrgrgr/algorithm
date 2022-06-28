def solution(people,limit):
  answer = 0
  people.sort()

  first = 0
  last = len(people)-1

  while first <= last:
    answer += 1
    if people[first] + people[last] <= limit:
      first += 1
      
    last -= 1 
  
  return answer

# indexing 으로 푸는 문제 x
# def solution(people, limit):
#   answer = []
#   tmp = []
#   people.sort()

#   tmp.append(people.pop(-1))
#   idx = -1
#   while people:
#     if len(tmp) == 2 or idx == -(len(people) + 1):
#       answer.append(tmp.copy())
#       tmp.clear()
#       tmp.append(people.pop(-1))
#       if not people:
#         answer.append(tmp.copy())
#         tmp.clear()
#         break
#       idx = -1
#     if sum(tmp) + people[idx] > limit:
#       idx -= 1
#     else:
#       tmp.append(people.pop(idx))
#       idx = -1

#   if tmp:
#     answer.append(tmp)
#   print(answer)
#   return len(answer)

solution([10,30,21,44,65,55],150)