def groupkey(key1):
 for i in range(len(key1)):
  if(key1.keys()=="id"):
    count=1
 if count!=1: 
  udate_dict={'groupmembership':{'values':[{'group':{'id':"null"}}]}}
  x.update(udate_dict)
 count1=0
 for i in range(len(key1)):
  if(key1.keys()=="name"):
    count1=1
 if count1!=1: 
  udate_dict={'groupmembership':{'values':[{'group':{'name':"null"}}]}}
  x.update(udate_dict)


def edu_key(x1):
 for i in range(len(x1)):
    count=0;count1=0;count2=0;count3=0;count4=0
    a=x1[i]
    b=a.keys()
    for i1 in range(len(b)):
      if b[i1]=='fieldOfStudy':
         count=1
         break
    for i1 in range(len(b)):
      if b[i1]=='schoolName':
         count1=1
         break
    for i1 in range(len(b)):
      if b[i1]=='degree':
         count2=1
         break
    for i1 in range(len(b)): 
      if b[i1]=='endDate':
         count3=1
         break
    for i1 in range(len(b)):
      if b[i1]=='startDate':
         count4=1
         break
    if count!=1:
       update_dict={'fieldOfStudy':"null"}
       a.update(update_dict)
    if count1!=1:
       update_dict={'schoolName':"null"}
       a.update(update_dict)
    if count2!=1:
       update_dict={'degree':"null"}
       a.update(update_dict)
    if count3!=1:
       update_dict={'endDate':"null"}
       a.update(update_dict)
    if count4!=1:
       update_dict={'startDate':"null"}
       a.update(update_dict)


def company_key(a):
 for i in range(len(a)):
    count=0;count2=0;count3=0;count4=0
    a2=a[i]
    a3=a2.keys()
    for i1 in range(len(a3)):
       if a3[i1]=="timestamp":
         count=1
         break
    if count!=1:
      update_dict={"timestamp":"null"}
      a2.update(update_dict)
    for i1 in range(len(a3)):
       if a3[i1]=="numLikes":
         count2=1
         break
    for i1 in range(len(a3)):
       if a3[i1]=="updateContent":
         count3=1
         break
    for i1 in range(len(a3)):
       if a3[i1]=="updateComments":
         count4=1
         break
    if count2!=1:
      update_dict={"numlikes":"null"}
      a2.update(update_dict)
    if count3!=1:
      update_dict={"updateContent":"null"}
      a2.update(update_dict)
    if count4!=1:
      update_dict={"updateComments":"null"}
      a2.update(update_dict)
