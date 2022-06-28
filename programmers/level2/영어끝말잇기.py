from collections import deque
import math

def solution(n, words):
  answer = [] 
  words = deque(words)
  wordslist = []
  wordslist.append(words.popleft())

  while words:
    if words[0] in wordslist:
      who = (len(wordslist)+1)%n
      if who == 0:
        who = n
      turn = math.ceil((len(wordslist)+1)/n)
      return [who,turn]
    if wordslist[-1][-1] == words[0][0]:
      wordslist.append(words.popleft())
    else:
      who = (len(wordslist)+1)%n
      if who == 0:
        who = n
      turn = math.ceil((len(wordslist)+1)/n)
      return[who,turn]
  return [0,0]

# def solution(n, words):
#     for p in range(1, len(words)):
#         if words[p][0] != words[p-1][-1] or words[p] in words[:p]: return [(p%n)+1, (p//n)+1]
#     else:
#         return [0,0]