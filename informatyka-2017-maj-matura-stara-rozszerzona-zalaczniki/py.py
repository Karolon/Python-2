
file = open('binarne.txt')

data =[]
for f in file:
  data.append(f.strip())
  
longest = ''
amount = 0
for d in data:
  if len(d)%2 == 0:
    if d[0:len(d)//2] == d[len(d)//2:]:
      amount+=1
      if len(d) > len(longest):
        longest = d
  
print(amount, longest, len(longest))

biggest_bin = 0
biggest = 0
for f in data:
  b = int(f)
  i = int(f,2)
  if i <= 65535:
    if biggest < i:
      biggest=i
      biggest_bin = b
      
print(biggest_bin, biggest)


amount = 0
shortest = '0000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000'
for d in data:
  for i in range(len(d)//4):
    if int(d[4*i:4*i+4],2)>9:
      amount+=1
      if len(d) < len(shortest):
        shortest = d
      break
  
print(amount, len(shortest))