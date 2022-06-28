# R-4
k = int(input())
food_times = list(map(int, input().split()))

f_len = len(food_times)

ans = -1
idx = 0
sec = 0

# 시간(sec)이 k보다 작을 때까지 반복
while (sec <= k):
  idx = idx % len(food_times) # 인덱스 초기화
  if f_len == food_times.count(0):# k(네트워크 이슈)전에 음식 다 먹으면 종료
    ans = -1
    print(ans)
  # food times 배열을 순회하는데, 그 값이 0보다 크면 시간(sec)과 인덱스(idx)를 1 더하고,
  # food times 값은 1 줄임(먹었으니)
  # 계속 반복하다가 시간(sec) 랑 네트워크 이슈(k) 가 같아지면 그 때의 idx를 출력
  if food_times[idx] > 0: 
    food_times[idx] -= 1
    idx += 1
    sec += 1
  # 0 이면 그냥 인덱스만 더함, 시간은 안가고 다음 음식 먹은 것
  else:
    idx += 1

# 시간복잡도 n, 박광렬
ans = idx
print(ans)