def sprawdzanie(s):
  nawiasy = 0
  for i in s:
    if i == '(':
      nawiasy+=1
    if i == ')':
      if nawiasy == 0:
        return False
      nawiasy-=1
  if nawiasy == 0:
    return True
  else:
    return False

file = open('Nawiasy.txt')
file2 = open('zad6.txt', mode='w')
for f in file:
  f=f.strip()
  if sprawdzanie(f):
    print(f+' prawda', file=file2)
  else:
    print(f+' fałsz', file=file2)
file2.close()