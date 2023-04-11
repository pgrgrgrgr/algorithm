def solution(sequence, k):
  answer = []

  start, end = 0, 0
  min_len = 1000001

  acc = sequence[0]

  while start <= end < len(sequence):
    if start > end:
      acc = sequence[start]
      end = start
      continue

    if acc < k:
      end += 1
      if end < len(sequence):
        acc += sequence[end]
    elif acc > k:
      acc -= sequence[start]
      start += 1
    elif acc == k:
      if end - start + 1 < min_len:
        min_len = end - start + 1
        answer = [start, end]
      acc -= sequence[start]
      start += 1

  return answer

print(solution([1, 1, 1, 2, 3, 4, 5], 5))