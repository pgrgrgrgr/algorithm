def solution(n):
  answer = ''

  while n>0:
    if n%3 == 0:
      answer = '4'+answer
      n = int(n/3) -1
    else:
      answer = str(n%3) + answer
      n = int(n/3)
      
  return answer

# def change124(n):
#   num = ['1','2','4']
#   answer = ""


#   while n > 0:
#     n -= 1
#     answer = num[n % 3] + answer
#     n //= 3

#   return answer
# if문이 필요가 없음