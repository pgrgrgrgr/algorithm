def solution(skill, skill_trees):
  skill_dic={}
  skill_stack=[]
  tmp_stack=[]
  tmp_stack2=[]
  cnt=0
  tmp=''
  answer = 0

  for i in skill:
    skill_dic[i]=cnt
    cnt+=1
  
  for str in skill_trees:
    for i in str:
      if i in skill:
        tmp+=i
    skill_stack.append(tmp)
    tmp=''
  print(skill_stack)

  for str in skill_stack:
    for i in str:
      tmp_stack.append(skill_dic[i])
    if tmp_stack == sorted(tmp_stack):
      answer += 1
      while(tmp_stack):
        tmp_stack2.append(tmp_stack.pop())
        if(len(tmp_stack)==0):
          if(tmp_stack2[-1]!=0):
            answer-=1
          break
        if(tmp_stack2[-1]-1!=tmp_stack[-1]):
          answer-=1
          break
    tmp_stack.clear()
    tmp_stack2.clear()
      
  return answer

solution("CBD",["BACDE", "CBADF", "AECB", "BDA"])
