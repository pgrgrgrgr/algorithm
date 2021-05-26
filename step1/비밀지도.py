def solution(n, arr1, arr2):
  answer = ['']*n
  for i in range(len(arr1)):
    arr1[i] = bin(arr1[i]).lstrip('0b')
    arr1[i] = arr1[i].zfill(n)
  for i in range(len(arr2)):
    arr2[i] = bin(arr2[i]).lstrip('0b')
    arr2[i] = arr2[i].zfill(n)
  for i in range(n):
    for j in range(n):
      if str(int(arr1[i][j])|int(arr2[i][j])) == '1':
        answer[i] += '#'
      else:
        answer[i] += ' '

  return answer

# def solution(n, arr1, arr2):
#   answer = []*n
#   for i,j in zip(arr1,arr2):
#     new = str(bin(i|j)[2:])
#     new = new.zfill(n)
#     answer.append(new)
#   for i in range(n):
#     answer[i] = answer[i].replace('1','#')
#     answer[i] = answer[i].replace('0',' ')
#   return answer
