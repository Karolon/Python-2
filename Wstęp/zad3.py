file = open('Liczby_binarne.txt')

data = []
for f in file:
  data.append(f.strip())

def bin_to_for(n):
  n = n[2:]
  anser=0
  for i in range(len(n[2:])):
    x = int(n[-i])*2
    if x == 4:
      x = 10
    anser+=x*(10**(i//2))
  return anser
  
amount1, amount2, amount3, amount4, biggest = 0,0,0,0,0
smallest = 999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
int_sum, sum100 = 0,0
for d in data:
  if d[-1] == '0':
    amount1+=1
  else:
    amount3+=1
  if int(d,2)%8 == 0:
    amount2+=1
  if len(d) == 7:
    amount4+=1
    int_sum += int(d,2)
  if int(d) > biggest:
    biggest = int(d)
  if int(d) < smallest:
    smallest = int(d)
    
for d in data[:100]:
  sum100 += int(d,2)


file = open('zad3.txt', mode='w')
print('a '+str(amount1)+' '+str(amount2), file=file)
print('b '+str(amount3), file=file)
print('c',str(amount4),str(bin(int_sum)[2:]),str(int_sum),str(bin_to_for(str(bin(int_sum)))), file=file, sep=' ')
print('d '+str(sum100), file=file)
print('e '+str(biggest)+' '+str(smallest), file=file)
file.close()