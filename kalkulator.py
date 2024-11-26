def not_fun():
  def dec2bin(x):
    y = ''
    while x > 0:
      y = '01'[x % 2] + y
      x //= 2
    return y

  n = float(input('liczba \n'))
  ile = int(input('jaka dokladnosc?\n'))

  a = int(n)
  b = n-a
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