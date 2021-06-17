def solution(progresses, speeds):
  answer = []
  queue=[]
  while progresses:
    while progresses[0] < 100:
      for i in range(len(progresses)):
        progresses[i] += speeds[i]

    queue.append(progresses.pop(0))
    speeds.pop(0)

    if not progresses or progresses[0]<100:
      answer.append(len(queue))
      queue.clear()

  return answer