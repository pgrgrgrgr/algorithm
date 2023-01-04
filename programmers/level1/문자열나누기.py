def solution(s):
  answer = 0
  check = [0, 0]
  tmp = s[0]
  
  for i in range(len(s)):
    if(i == len(s)-1):
      answer += 1
      break
    if(tmp == s[i]):
      check[0] += 1
    else:
      check[1] += 1
    if(check[0] == check[1]):
      answer += 1
      tmp = s[i+1]
      check = [0, 0]

  return answer

print(solution("bananas"))