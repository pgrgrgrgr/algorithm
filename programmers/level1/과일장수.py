def solution(k, m, score):
  answer = 0
  score = (sorted(score))
  sum_score = []

  while(len(score) >= m):
    for i in range(m):
      sum_score.append(score.pop())
    answer += sum_score[-1] * m
    sum_score.clear()
  return answer

print(solution(4, 3, [4, 1, 2, 2, 4, 4, 4, 4, 1, 2, 4, 2]))