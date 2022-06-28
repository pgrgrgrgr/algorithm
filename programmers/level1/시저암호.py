from string import ascii_uppercase
from string import ascii_lowercase

def solution(s, n):
  answer = ''
  lowerlist = list(ascii_lowercase)
  upperlist = list(ascii_uppercase)
  for i in range(len(s)):
    if s[i] in lowerlist:
      answer += lowerlist[(lowerlist.index(s[i])+n)%26]
    elif s[i] in upperlist:
      answer += upperlist[(upperlist.index(s[i])+n)%26]
    else:
      answer += " "
  return answer