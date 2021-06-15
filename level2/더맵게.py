def solution(scoville, K):
  answer = 0
  
  while min(scoville) < K:
    try:
      scoville.sort()
      mixed = scoville[0] + scoville[1] * 2
      scoville.remove(scoville[0])
      scoville.remove(scoville[0])
      scoville.append(mixed)
      answer += 1
    except IndexError:
      return -1

  return answer