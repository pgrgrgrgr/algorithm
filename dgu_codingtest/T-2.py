# 선형 탐색은 O(n) 요구하니까, 이진 탐색 구현
def binary_search(start, end, target, progression):
  while start <= end:
    mid = (start + end) // 2

    if progression[mid] == target:
      return mid
    
    if progression[mid] > target:
      end = mid - 1
    elif progression[mid] < target:
      start = mid + 1
  return 0

N, x = map(int, input().split())
progression = list(map(int, input().split()))

start = 0
end = N - 1

# 어차피 정렬되어 있는 수열이므로, 타겟보다 1 작은 값이랑 (이 때 이진 탐색은 end를 줄이게 되므로 타겟보다 1 작은값의 마지막 인덱스를 찾을 것)
# 타겟보다 1 큰 값의 (이 때는 start를 늘리므로 큰 값의 첫 인덱스를 찾을 것) 인덱스를 찾아서, 그 차이를 계산
first = binary_search(start, end, x-1, progression)
final = binary_search(start, end, x+1, progression)

ans = (final - 1) - (first + 1) + 1

if (final - first) > 0:
  print(ans)
else:
  print(-1)
# 시간복잡도 log n, 박광렬