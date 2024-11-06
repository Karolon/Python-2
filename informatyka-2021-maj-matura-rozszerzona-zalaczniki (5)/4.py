file = open('instrukcje.txt')

napis = []
longest =['',0]
longest2 = ['',1]
old_ins = ''
letter_number = [0]*26
for f in file:
  f = f.strip().split()
  if f[0] == 'DOPISZ':
    letter_number[ord(f[1])-ord('A')] += 1
    napis.append(f[1])
  if f[0] == 'ZMIEN':
    napis[-1] = f[1]
  if f[0] == 'USUN':
    del napis[-1]
  if f[0] == 'PRZESUN':
    i=0
    while napis[i] != f[1]:
      i+=1
    if napis[i] == 'Z':
      napis[i] = 'A'
    else:
      napis[i] = chr(ord(napis[i])+1)
  if old_ins == f[0]:
    longest2[0] = f[0]
    longest2[1] += 1
    if longest[1] < longest2[1]:
      longest = longest2
  else:
    longest2 = ['',1]
  old_ins = f[0]
  
  
  
    
print(chr(ord('A') + letter_number.index(max(letter_number))), max(letter_number))
print(*longest)
print(*napis, sep='')
print(len(napis)) 