n = int(input())
old_y = 0
old_x = 0
plakaty = 0
low_y = 0
cos = []
for i in range(n):
  flag = True
  x,y = input().split()
  x,y = int(x), int(y)
  if i == 0 or low_y < y:
    low_y = y
  if y > old_y:
    plakaty += 1
    cos.append(y)
  elif y < old_y:
    cos2 = []
    cos2.append(cos)
    while y < cos2[i]:
      del cos2[i]
    if not y in cos2:
      plakaty+=1
      flag = False
  if low_y < y and old_y > y and flag:
    plakaty+=1
  old_y = y


print(plakaty)