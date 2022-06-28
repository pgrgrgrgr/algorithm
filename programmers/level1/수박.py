import itertools

def solution(n):
  answer = ''
  wmcycle = itertools.cycle(['수','박'])
  for i in range(n):
    answer += next(wmcycle)
  return answer

solution(10)