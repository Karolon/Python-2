x = input()

def lider(x):
  lider = ['',0]

  flag = True
  for i in x:
    c = x.count(i)
    if c > lider[1]:
      flag = True
      lider = [i,c]
    elif c == lider[1]:
      if lider[0] != i:
        flag = False
        
  if flag:
    return lider
  return[None,'']

print(*lider(x))


def lider2(x):
  liders = []
  letters = []
  letter_amount = []
  flag = True
  for i in x:
    if not i in letters:
      c = x.count(i)
      letter_amount.append(c)
      
  lida = []
  maximum = max(letter_amount)
  for i in range(len(letters)):
    if letter_amount[i] == maximum:
      lida.append([letters[i], letter_amount[i]])
    
        
  if flag:
    return lida
  return[None,'']