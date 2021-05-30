def solution(s):
  answer = ''
  s = sorted(s,reverse=1)
  for i in s:
    answer += i
  return answer