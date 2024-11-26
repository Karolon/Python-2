
#a
n ="Przystojny Jarek bardzo nie lubi jeść jabłek"
n = n.split()
def ileSlow(n):
  amount = 0
  for i in range(len(n)-1):
    for j in n[i+1:]:
      if len(n[i]) != len(j):
        amount += 1
  return amount
print(ileSlow(n))

#b
file = open('TrójkaMiłośnikówLiteratury.txt')
data = []
i=0
for f in file:
  data.append(f.strip().split())
  
words = []
for d in data:
  for l in d:
    words.append(l)

words2 = []
for d in data[:5]:
  for l in d:
    words2.append(l)
print(ileSlow(words2))

#c
def zrobSlowo(a,b):
  ans = ''
  if len(a) == len(b):
    return 'NIE MOŻNA'
  elif len(a) > len(b):
    ans = a+'X'+'V'*(len(a)+len(b))+'X'+b
  else:
    ans = b+'X'+'V'*(len(a)+len(b))+'X'+a
  return ans

slowo1 = zrobSlowo(words[0],words[-1])
slowo2 = zrobSlowo(words[248],words[249])
print(slowo1)
print(slowo2)
print(zrobSlowo(slowo1,slowo2))
#d
def cyborg(slowo1,slowo2):
  slowo = zrobSlowo(slowo1,slowo2)
  if slowo == 'NIE MOŻNA':
    return 'NIE MOŻNA'
  suma = 0
  for i in range(len(slowo)):
    if slowo[i] == 'V':
      suma += 5
    elif slowo[i] == 'X':
      suma+=10
  slowo = slowo.replace('X',"")
  slowo = slowo.replace('V',"")
  zmienna = 'a'
  for i in range(2,suma):
    if suma%i == 0:
      zmienna = 'b'
  if len(slowo1) > len(slowo2):
    ans = slowo1+zmienna+slowo2
  elif len(slowo1) < len(slowo2):
    ans = slowo2+zmienna+slowo1
  return ans

print(cyborg(words[0],words[-1]))