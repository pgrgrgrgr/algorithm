def solution(numbers):  
  answer = ''
  cnt=1
  
  if numbers.count(0)==len(numbers):
    return "0"
  
  for i in range(0,len(numbers)):
    numbers[i]=str(numbers[i]) 
  numbers.sort(reverse=True)
  
  while cnt<=len(numbers)-1:
    if numbers[cnt]+numbers[cnt-1] > numbers[cnt-1]+numbers[cnt]:
      a=numbers[cnt-1]
      numbers[cnt-1]=numbers[cnt]
      numbers[cnt]=a
      cnt-=2
    cnt+=1

  for i in range(0,len(numbers)):
    answer+=numbers[i]
  
  return answer

# def solution(numbers):
#   numbers = sorted(list(map(str, numbers)), key=lambda x: x*3, reverse=True)
#   print(numbers)
#   return str(int(''.join(numbers)))