def solution(n, m):
  answer = []
  binlist=[]
  binlist2=[]
  for i in range(min(n,m)):
    if (n%(i+1)) == 0 and (m%(i+1)) == 0:
      binlist.append(i+1)
    if (m*(i+1))%n == 0:
      binlist2.append(m*(i+1))
  answer.append(max(binlist))
  answer.append(min(binlist2))
  return answer

# def gcdlcm(a, b):
#   c, d = max(a, b), min(a, b)
#   t = 1
#   while t > 0:
#       t = c % d
#       c, d = d, t
#   answer = [c, int(a*b/c)]
#   return answer
# euclidean algorithm