def solution(a, b):
  answer = ''
  # 1월31일 2월29일 3월31 4월30 5월31 6월30 7월31 8월31 9월30 10월31 11월30 12월31
  # 1월1일은 금요일
  daydic={4:'MON',5:'TUE',6:'WED',0:'THU',1:'FRI',2:'SAT',3:'SUN'}
  if a==1:
    answer = daydic[b%7]
  elif a==2:
    answer = daydic[(b+31)%7]
  elif a==3:
    answer = daydic[(b+60)%7]
  elif a==4:
    answer = daydic[(b+91)%7]
  elif a==5:
    answer = daydic[(b+121)%7]
  elif a==6:
    answer = daydic[(b+152)%7]
  elif a==7:
    answer = daydic[(b+182)%7]
  elif a==8:
    answer = daydic[(b+213)%7]
  elif a==9:
    answer = daydic[(b+244)%7]
  elif a==10:
    answer = daydic[(b+274)%7]
  elif a==11:
    answer = daydic[(b+305)%7]
  elif a==12:
    answer = daydic[(b+335)%7]
  return answer

# import datetime

# def solution(a,b):
  # days = ['MON','TUE','WED','THU','FRI','SAT','SUN']
  # answer = days[datetime.date(2016,a,b).weekday()]
  # return answer 
  
