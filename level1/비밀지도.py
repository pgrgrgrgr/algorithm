def solution(n, arr1, arr2):
  answer = []*n
  for i,j in zip(arr1,arr2):
    new = str(bin(i|j)[2:])
    new = new.zfill(n)
    answer.append(new)
  for i in range(n):
    answer[i] = answer[i].replace('1','#')
    answer[i] = answer[i].replace('0',' ')
  return answer

solution(6,[46,33,33,22,31,50],[27,56,19,14,14,10]) 
