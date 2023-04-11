T = int(input())
t = 0

for _ in range(T):
  N, K = map(int, input().split())
  str = input()
  hexes = list()

  unit = int(N/4)
  
  for i in range(unit):
    str += str[i]

  for i in range(len(str) - 2):
    hexes.append(str[0+i:unit+i])
  hexes = list(set(hexes))

  for i in range(len(hexes)):
    hexes[i] = int(hexes[i], 16)
  hexes = list(reversed(sorted(hexes)))

  answer = hexes[K-1]

  print(f'#{_+1}', answer)
