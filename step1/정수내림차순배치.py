def solution(n):
  answer = ''
  nsort = list(map(int,sorted(str(n))))
  nsort.reverse()
  for i in nsort:
    answer += str(i)
  return int(answer)