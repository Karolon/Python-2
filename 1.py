file = open(file ='sygnaly.txt', mode='r')

data = []
for f in file:
  data.append(f.strip())

anser1 =[]
for i in range(39,len(data),40):
  anser1.append(data[i][9]) 
  
anser2=[]
wordN=[]
for d in data:
  wordN=[]
  for l in d:
    wordN.append(ord(l))
  if (max(wordN) - min(wordN)) <= 10:
    anser2.append(d)
    
print(anser2)
  
  
  
  




file = open(file='plik.txt', mode='w')
print(anser1, file=file)
print(len(anser2))
