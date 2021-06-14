def solution(s):
  answer = ''
  s = sorted(s,reverse=1)
  for i in s:
    answer += i
  return answer

# sorted 는 list로 변환 후 정렬