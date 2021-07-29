def solution(phone_book):
  answer = True
  pb_dic = {}
  for phone_num in phone_book:
    pb_dic[phone_num] = 1

  for phone_num in phone_book:
    tmp = ""
    for number in phone_num:
      tmp += number
      if tmp in pb_dic and tmp != phone_num:
        answer = False
        
  return answer