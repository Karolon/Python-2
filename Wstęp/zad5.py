file = open('Pesele.txt')

data = []
for f in file:
  data.append(f.strip())
  

date = 0
male = 0
birth1966=0
for d in data:
  if d[4:6] == '24' and int(d[-2])%2 != 0:  
    date+=1
  if int(d[-2])%2 != 0:
    male+=1
  if d[0:2] == '66' and (d[2] == '0' or d[2] == '1'):
    birth1966 +=1

    
file = open('zad5.txt', mode='w')
print('a '+str(date), file=file)
print('b',male,len(data)-male,sep=" ", file=file)
print('c '+str(birth1966), file=file) 
file.close() 