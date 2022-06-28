# R-2

n = int(input())
arr_A = list(map(int, input().split()))
arr_B = []

# 그냥 문제 설명에 있는 점화식 그대로...
for i in range(len(arr_A)):
  for k in range(i+1, len(arr_A)):
    if(arr_A[i] < arr_A[k]):
      arr_B.append(k)
      break

# 시간복잡도 n^2, 박광렬
print(arr_B)