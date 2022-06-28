import re

def solution(arr):
  answer = []
  binstr=''
  for i in range(len(arr)):
    binstr += str(arr[i])
  for i in range(10):
    binstr = re.sub('%d+'%i,'%d '%i,binstr)
  answer = list(map(int,binstr.split()))
  return answer 