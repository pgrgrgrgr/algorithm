def solution(maps):
  answer = 0
  mapdic = {}
  routecnt = 0
  number_1 = maps.count(1)
  for i in range(len(maps[0])):
    for j in range(len(maps)):
      mapdic[(i,j)] = maps[len(maps)-1-j][i]
  
  (px,py) = (0,len(maps)-1)
  while (px,py) != (len(maps)-1,0):
    if rightcheck(mapdic,px,py) == True:
      mapdic[(px,py)] = 0
      (px,py) = (px+1,py)
      routecnt += 1
    if downcheck(mapdic,px,py) == True:
      mapdic[(px,py)] = 0
      (px,py) = (px,py-1)
      routecnt += 1
    if leftcheck(mapdic,px,py) == True:
      mapdic[(px,py)] = 0
      (px,py) = (px-1,py)
      routecnt += 1
    if upcheck(mapdic,px,py) == True:
      mapdic[(px,py)] = 0
      (px,py) = (px,py+1)
      routecnt += 1
    if (px,py) == (len(maps[0]),0):
      break
    if routecnt >= number_1:
      break
  
  print(routecnt)
  return answer

def leftcheck(mapdic,px,py):
  if mapdic[(px-1,py)] == 1:
    return True
  else:
    return False

def rightcheck(mapdic,px,py):
  if mapdic[(px+1,py)] == 1:
    return True
  else:
    return False

def upcheck(mapdic,px,py):
  if mapdic[(px,py+1)] == 1:
    return True
  else:
    return False

def downcheck(mapdic,px,py):
  if mapdic[(px,py-1)] == 1:
    return True
  else:
    return False

solution([[1,0,1,1,1],[1,0,1,0,1],[1,0,1,1,1],[1,1,1,0,1],[0,0,0,0,1]])