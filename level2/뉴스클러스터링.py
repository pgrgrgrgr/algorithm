from string import ascii_lowercase

def solution(str1, str2):
  strcheck = 0
  andcheck = 0
  orcheck = 0
  str1 = str1.lower()
  str2 = str2.lower()
  sliced_str1 = []
  sliced_str2 = []

  for i in range(len(str1)-1):
    sliced_str1.append(str1[i:i+2])
  for i in range(len(str2)-1):
    sliced_str2.append(str2[i:i+2])

  while True:
    try:
      if sliced_str1[strcheck][0] not in ascii_lowercase or sliced_str1[strcheck][1] not in ascii_lowercase:
        sliced_str1.remove(sliced_str1[strcheck])
      else:
        strcheck += 1
    except IndexError:
      strcheck=0
      break
  while True:
    try:
      if sliced_str2[strcheck][0] not in ascii_lowercase or sliced_str2[strcheck][1] not in ascii_lowercase:
        sliced_str2.remove(sliced_str2[strcheck])
      else:
        strcheck += 1 
    except IndexError:
      break

  strtmp = sliced_str2.copy()
  
  for i in sliced_str1:
    if i in strtmp:
      andcheck += 1
      strtmp.remove(i)
  
  orcheck = len(sliced_str1) + len(sliced_str2) - andcheck
  if orcheck == 0:
    return 65536

  return int(andcheck / orcheck * 65536)

# def solution(str1, str2):

#     list1 = [str1[n:n+2].lower() for n in range(len(str1)-1) if str1[n:n+2].isalpha()]
#     list2 = [str2[n:n+2].lower() for n in range(len(str2)-1) if str2[n:n+2].isalpha()]

#     tlist = set(list1) | set(list2)
#     res1 = [] #합집합
#     res2 = [] #교집합

#     if tlist:
#         for i in tlist:
#             res1.extend([i]*max(list1.count(i), list2.count(i)))
#             res2.extend([i]*min(list1.count(i), list2.count(i)))

#         answer = int(len(res2)/len(res1)*65536)
#         return answer

#     else:
#         return 65536