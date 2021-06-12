def solution(arr1, arr2):
  answer = []
  for i in range(len(arr1)):
    for j in range(len(arr2[0])):
      answer.append((arr1[i][j]+arr2[i][j]))

  answer = [answer[len(arr1[0])*i:len(arr1[0])*(i+1)] for i in range(len(arr1))]
  return answer