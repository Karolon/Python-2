#1
file_ans = open('wyniki3.txt', 'w')
file = open('pi.txt')

old = -1
amount = 0
fragmenty = [0]*100
last6 = [0]*6

for f in file:
  f = int(f.strip())
  part = [old, f]
  part2 = old*10+f
  fragmenty[part2] +=1
  if part2 > 90:
    amount += 1
  old = f
  
print(amount, file=file_ans)

#2

minimal = str(fragmenty.index(min(fragmenty)))
if len(minimal) == 1:
  minimal = '0'+str(minimal)
print(minimal, fragmenty[int(minimal)], file=file_ans)

maximal = str(fragmenty.index(max(fragmenty)))
if len(maximal) == 1:
  maximal = '0'+str(maximal)
print(maximal, fragmenty[int(maximal)], file=file_ans)




file.close()
