def solution(priorities, location):
  answer = 0
  location_array = [i for i in range(len(priorities))]
  priorities_copy = priorities.copy()
  cnt = 0

  while True:
    if priorities_copy[cnt] < max(priorities_copy[cnt+1:]):
      location_array.append(location_array.pop(cnt))
      priorities_copy.append(priorities_copy.pop(cnt))
    else:
      cnt += 1

    if priorities_copy == sorted(priorities_copy, reverse=True):
      break
  
  answer = location_array.index(location) + 1

  return answer