N, M = map(int, input().split())
N_list = list(map(int, input().split()))

H = max(N_list)

# 주어진 떡들 중 최대 길이를 지정하고, 1씩 줄여가며 가능한 길이 계산
while True:
  H_sum = 0
  for i in N_list:
    if (i > H):
      H_sum += i - H

  if (H_sum < M):
    H -= 1
  else:
    print(H)
    break

# 하나의 떡이 비교적 큰 수인 경우가 최악
# 시간복잡도 n, 박광렬