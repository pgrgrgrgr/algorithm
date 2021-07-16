def solution(clothes):
  answer = 0
  clothes_count = {}
  for i in clothes:
    if i[1] in clothes_count: 
      clothes_count[i[1]] += 1
    else: 
      clothes_count[i[1]] = 1

  noc=1

  for i in clothes_count.values():
    noc = noc * (i+1)

  answer = noc - 1
  return answer

solution(	[["yellow_hat", "headgear"], ["blue_sunglasses", "eyewear"], ["green_turban", "headgear"]])