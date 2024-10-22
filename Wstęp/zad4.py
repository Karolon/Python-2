file = open('Liczby_osemkowe.txt')

def pokolei(n):
  old = n[0]
  for i in n:
    if int(old) > int(i):
      return(False)
    old = i
  return True

amount1, amount2, amount3, amount4 = 0,0,0,0
data = []
for f in file:
  data.append(f.strip())
  
for d in data:
  if d[0] == d[-1]:
    amount1+=1
  if str(int(d,8))[0] == str(int(d,8))[-1]:
    amount2+=1
  if pokolei(d):
    amount3+=1
  if int(d)%2 == 0:
    amount4 += 1

file = open('zad4.txt', mode='w')
print('a '+str(amount1), file=file)
print('b '+str(amount2), file=file)
print('c '+str(amount3), file=file)
print('d '+str(amount4), file=file)
file.close()