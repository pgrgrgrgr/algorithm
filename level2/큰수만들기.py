def solution(number, k):
  answer = ''
  answer_length = len(number) - (k-1)
  tmp='0'
  idcnt=0
  while len(answer) != answer_length - 1:
    end = -(answer_length-len(answer)-2)
    for i in range(len(number[0:end])):
      if tmp < number[i]:
        tmp = number[i]
        idcnt = i
      if tmp == '9':
        break
    answer += tmp
    tmp = '0'

    number = number[0:idcnt] + number[idcnt+1:]
  print(answer)
  return answer

solution('4177252841',4)