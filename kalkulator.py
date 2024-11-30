def decToBin_calc():
  def dec2bin(x):
    y = ''
    flag = x<0
    x = x if x >=0 else x*(-1)
    while x > 0:
      y = '01'[x % 2] + y
      x //= 2
    y = '-' + y if flag else y
    return y

  n = float(input('liczba \n').replace(',','.'))
  ile = int(input('jaka dokladnosc?\n'))

  a = int(n)
  b = n-a
  b = b if b >=0 else b*(-1)
  x = dec2bin(a)
  y = ''

  i = 1
  while i <= ile:
    if b >= 1 / (2 ** i) and b != 0.0:
      y += '1'
      b -= 1 / 2 ** i
    else:
      y += '0'
    i += 1

  ans = x + '.' + y

  print(ans)
  

def BinToDec_calc():
  def bin2dec(x):
    y = 0
    if x % 10 != 0:
      y += 1
    x //= 10
    i = 1
    while x > 0:
      y += int('02'[x % 10]) ** i
      x //= 10
      i += 1
    return y
  
  def BinFloat2Dec(x, ile):
    y = 0.0 
    i = 1
    while i < ile:
      x *= 10
      if x//1 != 0:
        y += 2 ** ((-1)*i)
      i += 1
      x = x-1 if int(x) == 1 else x
    return y
      
      
  n = float(input('liczba \n').replace(',','.'))
  ile = int(input('jaka dokladnosc?\n'))
  a = int(n)
  b = n-a
  x = bin2dec(a)
  y = BinFloat2Dec(b, ile)
  
  ans = f"{x+y:.{ile}f}"
  print(ans)


flag  = True
while flag:
  tmp = input('Z binarncyh na dziesiętne - D\nZ dziesiętnych na binarne - B\n').lower()
  if tmp in ['b','bin']:
    decToBin_calc()
    flag = False
  elif tmp in ['d','dec']:
    BinToDec_calc()
    flag = False
  else:
    print('Wow, udało ci się niepoprawnie wpisać literke "B" albo "D"')