file = open('dane.txt')


def isPrime(n):
  if n < 2:
    return False
  if n == 2:
    return True
  for i in range(3, n//2 + 1, 2):
    if n % i == 0:
      return False
  return True

def najdłuższe_słowo_w_języku_polskim(n):
  count = 0
  for i in range(n):
    if isPrime(i):
      if n % 2 == 0:
        count += 1
        n //= i
  return count >= 4
  
def konstyntanopolitańczykowianeczka(n):
  a = int(''.join(sorted(str(n))))
  b = int(''.join(sorted(str(n), reverse = True)))
  if abs(a - b) < n:
    return 0
  elif abs(a - b) > n:
    return 2
  else:
    return 1
    
róznica = [0, 0, 0] #mniejsza równa większa
primes = []
maks_znaki = ['', 0, 0] #słowo, wiersz, długość
wiersz = 1
dzielniki = []

for f in file:
  f = f.strip().split()
  f[0] = int(f[0])
  
  if isPrime(f[0]):
    primes.append(f[0])
    
  znaki = len(set(f[1]))
  if maks_znaki[2] < znaki:
    maks_znaki = [f[1], wiersz, znaki] 
  
  róznica[konstyntanopolitańczykowianeczka(f[0])] += 1
    
  if najdłuższe_słowo_w_języku_polskim(f[0]):
    dzielniki.append(f[0])
  
  wiersz += 1








file_ans = open('wyniki_Karol_Leyk.txt', 'w')

print('#1', file = file_ans)
print('róznica:', max(primes) - min(primes), file = file_ans)
leng = len(primes)
primes.sort()
if leng % 2 == 0:
  print('mediana:', (primes[leng//2-1] + primes[leng//2])/2, file = file_ans)
else:
  print('mediana:', primes[leng//2+1], file = file_ans)

print('\n#2', file = file_ans)
print('napis:', maks_znaki[0], file = file_ans)
print('wiersz:', maks_znaki[1], file = file_ans)

print('\n#3', file = file_ans)
print('mniejsze:',róznica[0], file = file_ans)
print('więkrze:',róznica[2], file = file_ans)
print('równe:',róznica[1], file = file_ans)

print('\n#4', file = file_ans)
print(*dzielniki, file = file_ans)


file_ans.close()












































