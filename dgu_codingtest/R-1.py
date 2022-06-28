# R-1

n = int(input())

arr = list(map(int, input().split()))
arr = sorted(arr)

res = 0 # 총 파티 수
cnt = 0 # cnt는 파티에 포함된 모험가의 수

# 모험가들(arr)을 하나씩 보며, 현재 파티에 포함된 모험가의 수가 현재의 공포도 이상인 경우만 파티 맺기
for i in arr:
  cnt += 1
  if (cnt >= i):
    res += 1
    cnt = 0

# 시간복잡도 n^2, 박광렬
print(res)