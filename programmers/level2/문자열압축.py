def solution(s):
  answer = 0
  sliced_tmp = ''
  answer_tmp = ''
  answer_list = []

  if len(s) == 1:
    return 1
    
  for slice in range(1,int(len(s)/2) + 1):
    sliced_tmp = s[:slice]
    cnt=1

    for i in range(slice, len(s), slice):
      if sliced_tmp == s[i:i+slice]:
        cnt += 1

      else:
        if cnt == 1:
          cnt = ''
          answer_tmp += cnt + sliced_tmp
          sliced_tmp = s[i:i+slice]
          cnt = 1
        else:
          answer_tmp += str(cnt) + sliced_tmp
          sliced_tmp = s[i:i+slice]
          cnt = 1

    if cnt == 1:
      cnt = ''
      answer_tmp += cnt + sliced_tmp
    else:
      answer_tmp += str(cnt) + sliced_tmp
      cnt = 1

    answer_list.append(len(answer_tmp))
    answer_tmp = ''

  answer = min(answer_list)
  return answer

solution("ababcdcdababcdcd")