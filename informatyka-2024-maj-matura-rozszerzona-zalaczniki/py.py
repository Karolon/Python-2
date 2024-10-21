file = open("skrot.txt")
file2 = open("wyniki3_2.txt")

def skrot(n):
  m = ''

  for i in n:
    if int(i)%2 != 0:
      m+= i
    
  if  m == '':
    return False
  else:
    return m

data = []
for f in file:
  data.append(f.strip())
  
n=0
amount=0
for d in data:
  if not skrot(d):
    amount+=1
    if int(d)>n:
      n=int(d)
print(amount,n)