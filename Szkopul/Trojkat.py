x,y,z = input().split()
x,y,z = int(x),int(y),int(z)
if x < y+z and y < x+z and z < x+y:
  print('TAK')
else:
  print('NIE')