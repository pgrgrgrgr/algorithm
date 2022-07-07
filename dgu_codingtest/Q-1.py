arr = list(map(int, input().split()))

asc = [1, 1]
desc = [1, 1]

for i in range(len(arr) - 1):
  if(arr[i] < arr[i+1]):
    asc[0] += 1
    desc[0] = 1
    if(asc[1] < asc[0]):
      asc[1] = asc[0]
  elif(arr[i] > arr[i+1]):
    desc[0] += 1
    asc[0] = 1
    if(desc[1] < desc[0]):
      desc[1] = desc[0]
  else:
    asc[0] = 1
    desc[0] = 1

print(asc[1], desc[1])