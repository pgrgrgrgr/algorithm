def solution(record):
  answer = []
  ch_record=[]
  id_dic={}
  
  for i in record:
    i = i.split(" ")
    ch_record.append(i)

  for i in range(len(ch_record)):
    if "Enter" in ch_record[i]:
      id_dic[ch_record[i][1]] = ch_record[i][2]
    elif "Change" in ch_record[i]:
      id_dic[ch_record[i][1]] = ch_record[i][2]

  for i in ch_record:
    if "Enter" in i:
      answer.append("%s님이 들어왔습니다."%id_dic[i[1]])
    elif "Leave" in i:
      answer.append("%s님이 나갔습니다."%id_dic[i[1]])

  return answer