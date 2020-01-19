with open("TwoWaitsData.txt") as f:
  a="abcdefghijklmnopqrstuvwxyz-"
  count=0
  while f.readline():
    count+=1
  f.seek(0)
  
  p=[]
  for i in range(count+1):
    read=f.readline()
    m=read.split(" ")
    for j in m:
      p.append(j)

  t=[]
  for e in p:
    w=""
    for b in e:
      j=b.lower()
      if j in a:
        w+=b
    t.append(w)


    
  n=input("enter a word from text: ")
  
  number=t.count(n)
  print(f"The number of occurences of {n} is {number}.") 
  



