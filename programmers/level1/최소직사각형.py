def solution(sizes):
  width = []
  height = []
  for i in range(len(sizes)):
    if sizes[i][0] < sizes[i][1]:
      sizes[i] = list(reversed(sizes[i]))

    width.append(sizes[i][0])
    height.append(sizes[i][1])

  answer = max(width) * max(height)
  return answer

# def solution(sizes):
    return max(max(x) for x in sizes) * max(min(x) for x in sizes)

# solution = lambda sizes: max(sum(sizes, [])) * max(min(size) for size in sizes)
