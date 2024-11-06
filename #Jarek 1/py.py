file = open('Zabawa.txt')

letter_numb = [0]*26
data = []
for f in file:
  f = f.strip().split()
  letter_numb[ord(f[0][0])-ord('A')] += 1
  data.append(f)
  
guessedB = []
guessed = 0
guessedC = 0
for d in data:
  if str(letter_numb[ord(d[0][0])-ord('A')]) in d[1:]:
    guessed+=1
  if not str(letter_numb[ord(d[0][0])-ord('A')]) in d[1:] and len(d[0]) == 9:
    guessedB.append([d[0],min(abs(len(d[0])-int(d[1])),abs(len(d[0])-int(d[2])),abs(len(d[0])-int(d[3])))])
  if str(len(d[0])) in d[1:]:
    guessedC += 1
    
    
print(guessed)
print(*guessedB)
print(guessedC)