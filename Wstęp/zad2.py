file = open('Imiona.txt')

data = []
for f in file:
  data.append(f.strip())

  
damskie, męskie, amount1 = 0,0,0
first_letter = []
for d in data:
  if d[-1] == 'a':
    damskie+=1
  else:
    męskie+=1
  if d[0] == 'H' and len(d)<=8:
    amount1+=1
  first_letter.append(d[0])

letters = [0]*26
for i in range(26):
  letters.append(first_letter.count(chr(ord('A')+i)))
  
file = open('zad2.txt', mode='w')
print('a',damskie,męskie, file=file, sep=' ')
print('b ',amount1, file=file)
print('c', file=file)
for i in range(ord('Z')-ord('A')):
  print(chr(ord('A')+i),first_letter.count(chr(ord('A')+i)), file=file,sep=' ')
print(letters.index(max(letters))%26)
print('d ',chr(letters.index(max(letters))%26+ord('A')),max(letters), file=file)
file.close()