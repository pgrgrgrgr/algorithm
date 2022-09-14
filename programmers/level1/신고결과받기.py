def solution(id_list, report, k):
  answer = [0] * len(id_list)
  report = list(set(report))

  report_dic = {}
  for i in id_list:
    report_dic[i] = 0

  for i in report:
    a, b = i.split(' ')
    report_dic[b] += 1

  for i in report:
    a, b = i.split(' ')
    if(report_dic[b] >= k):
      answer[id_list.index(a)] += 1

  return answer
