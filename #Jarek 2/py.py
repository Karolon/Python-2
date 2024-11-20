
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
for d in data[:5]:
  for l in d:
    words.append(l)
print(words)
print(ileSlow(words))

#c
def zrobSlowo(n):
  pass