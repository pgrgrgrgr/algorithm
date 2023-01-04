def solution(s):
  answer = []
  dic = {}
  for idx, word in enumerate(list(s)):
    if word in dic:
      answer.append(idx - dic[word])
    else:
      answer.append(-1)
    dic[word] = idx
  return answer

print(solution("banana"))