with open("TwoWaitsData.txt") as f:
  read=f.read()
  readlist=read.split(" ")
  readlist.reverse()
  for i in readlist:
      print(i,end=" ")