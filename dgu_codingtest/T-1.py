N = int(input())
N_parts = list(map(int, input().split()))

M = int(input())
M_parts = list(map(int, input().split()))

# 손님의 요청 부품(M_parts)을 하나씩 순회하며, 가게의 부품(N_parts)에 있는 부품인지
for i in M_parts:
  if i in N_parts:
    print("yes", end=" ")
  else:
    print("no", end=" ")

# 시간복잡도 O(n), 박광렬