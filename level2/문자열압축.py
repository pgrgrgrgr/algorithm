def solution(s):
  answer = 0
  len_answertmp = []
  strtmp = ''
  answertmp = ''

  if len(s) == 1:
    return 1

  for slice in range(1, len(s)//2 + 1):
    cnt = 1
    strtmp = s[:slice]

    for tmp in range(slice, len(s), slice):
      if s[tmp:tmp+slice] == strtmp:
        cnt += 1
      else:
        if cnt == 1:
          cnt = ''
        answertmp += str(cnt) + strtmp
        strtmp = s[tmp:tmp+slice]
        cnt = 1

    if cnt == 1:
      cnt = ''
    answertmp += str(cnt) + strtmp

    len_answertmp.append(len(answertmp))
    answertmp = ''
  return min(len_answertmp)