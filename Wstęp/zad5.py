file = open('Pesele.txt')

data = []
for f in file:
  data.append(f.strip())
  

date = 0
male = 0
for d in data:
  if d[3:4] == 24:
    date+=1
  if int(d[-2])%2 == 0:
    male+=1
  

    
file = open('zad5.txt', mode='w')
print('a '+str(date), file=file)
print('b',male,len(d)-male,sep=" ", file=file)
print('c '+str(amount3), file=file)
print('d '+str(amount4), file=file)
file.close()