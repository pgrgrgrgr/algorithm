def solution(phone_book):
  answer = True
  phone_book.sort()
  pbdic = {}
  tmp=[]
  for i in range(len(phone_book)):
    pbdic[phone_book[i]] = len(phone_book[i])
  for i in sorted(set(pbdic.values())):
    for j in pbdic.keys():
      j = j[:i]
      tmp.append(j)
    if len(tmp) != len(set(tmp)) and len(tmp[1:]) == len(set(tmp[1:])):
      return False
    else:
      tmp.clear()


  return answer