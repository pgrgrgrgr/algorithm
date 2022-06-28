from collections import deque

def solution(prices):
  answer = []
  prices = deque(prices)
  prices_check = []
  cnt = 0

  while prices:
    prices_check.append(prices.popleft())
    
    for i in prices:
      if prices_check[-1] > i:
        cnt += 1
        break
      else:
        cnt += 1

    answer.append(cnt)
    cnt = 0

  return answer