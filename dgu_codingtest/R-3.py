# R-3

n = int(input())
arr_set = []

for i in range(n):
  arr_set.append(list(map(int, input().split())))
# 배열 [A,B] 를 입력받고, A를 기준으로 정렬함
arr_set = sorted(set, key = lambda x: (x[0]))


X = 0
# 역량값 X가 A보다 크면 B를 더함
for i in range(len(arr_set)):
  if(X >= arr_set[i][0]):
    X += arr_set[i][1]

if (X == 0):
  print(-1)
else:
  print(X)

# 시간복잡도 n^2, 박광렬