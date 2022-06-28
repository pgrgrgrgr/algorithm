def solution(number, k):
  answer = ''
  bignum = []

  for i in number:
    while bignum and bignum[-1] < i and k>0:
      k-=1
      bignum.pop()
    bignum.append(i)

  answer = "".join(bignum[:len(bignum)-k])

  return answer