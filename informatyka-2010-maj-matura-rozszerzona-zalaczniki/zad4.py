file = open("Dane\\anagram.txt")
file_ans = open('zadanie6.txt', 'w')

ansa = []
ansb = []
data = []
for f in file:
  data.append(f.strip().split())
  
for i in range(len(data)):
  if len(data[0]) == len(data[1]) == len(data[2]) == len(data[3]) == len(data[4]):
    ansa.append(i+1)
  if data[0].sort() == data[1].sort() == data[2].sort() == data[3].sort() == data[4].sort():
    ansb.append(data[i])  
  
print('a', file=file_ans)
print(*ansa, file=file_ans)
print('b', file=file_ans)
print(*ansb, file=file_ans)



file_ans.close()