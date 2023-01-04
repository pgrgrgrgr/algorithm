def solution(k, score):
  answer = []
  for i in range(len(score)):
    if(k >= i + 1):
      answer.append(min(sorted(score[0:i+1])))
    else:
      answer.append(list(reversed(sorted(score[0:i+1])))[k-1])
  return answer

# def solution(k, score):
#     q = []

#     answer = []
#     for s in score:

#         q.append(s)
#         if (len(q) > k):
#             q.remove(min(q))
#         answer.append(min(q))

#     return answer

print(solution(3, [10, 100, 20, 150, 1, 100, 200]))