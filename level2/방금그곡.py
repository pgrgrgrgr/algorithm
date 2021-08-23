import re
from datetime import datetime

def solution(m, musicinfos):
  answer = []
  musicarray = []
  timearray = []


  # #기호가 붙은 멜로디는 소문자로 치환
  for a in range(0,len(m)):
    m = list(m)
    if m[a] == '#':
      m[a-1] = m[a-1].lower()
    m = ''.join(m)
  for _ in musicinfos:
    _ = _.split(',')
    musicarray.append(_)
  for music in musicarray:
    tmp = list(music[3])
    for a in range(0,len(tmp)):
      if tmp[a] == '#':
        tmp[a-1] = tmp[a-1].lower()
    tmp = ''.join(tmp)
    music[3] = tmp
  
  if len(musicinfos)==1:
    return print(musicarray[0][2])

  # 음악이 재생된 시간 계산
  for _ in musicarray:
    t1 = datetime.strptime(_[0],'%H:%M')
    t2 = datetime.strptime(_[1],'%H:%M')
    timearray.append(str(t2-t1)[2:-3])
  
  # 재생된 음 계산
  for a in range(0,len(musicarray)):
    lyrics_len = len(musicarray[a][3])
    time = int(timearray[a])
    if time<lyrics_len:
      musicarray[a][3] = musicarray[a][3][:time]
    else:
      musicarray[a][3] = musicarray[a][3] * (time//lyrics_len) + musicarray[a][3][:time%lyrics_len]
  
  # 기억한 음이 방송된 노래 안에 있는지
  for a in musicarray:
    if m in a[3]:
      answer.append(a[2])

  if(len(answer)>1):
    return print(answer[timearray.index(max(timearray))])
  if(len(answer)==0):
    return print('(NONE)')
  return print(answer[0])
