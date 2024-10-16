data = input().split()
if (int(data[1])-int(data[0]))%int(data[2]) == 0:
  print((int(data[1])-int(data[0]))//int(data[2]))
else:  
  print((int(data[1])-int(data[0]))//int(data[2])+1)