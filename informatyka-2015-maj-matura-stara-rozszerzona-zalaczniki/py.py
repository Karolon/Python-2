file = open('aaa.txt')
data = []

for f in file:
  data.append(f.strip())

amont=0
for i in data:
  if i.count('0') > i.count('1'):
    amont+=1
    
print(amont)

amount=0
for i in data:
  if i[0] != 1:
    count = 0
    old_j = i[0]
    for j in i:
      if old_j == '0' and j == '1':
        count+=1
    if count==1:
      amount+=1
print(amount)