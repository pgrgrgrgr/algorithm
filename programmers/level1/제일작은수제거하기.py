def solution(arr):
  arr.remove(min(arr))
  return arr if len(arr)>1 else [-1]

# def rm_small(mylist):
#   return [i for i in mylist if i > min(mylist)]
# 현재는 컴프리헨션 조건에 만족하지않아도 -1을 반환하지 않기 때문에 안댐