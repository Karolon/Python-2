file = open("pary.txt")


def isPrime(n):
  for i in range(2, n//2):
    if n % i == 0:
      return False
  return True
  
def dzielniki(n):
  dz = []
  for i in range(1,n+1):
    if n % i == 1:
      dz.append(i)
  return dz

palindrom = ''
ndz = 0
dzzz = [1]
primes = []
data = []
for f in file:
  f = f.strip().split()
  f[0] = int(f[0])
  data.append(f[0])
  if isPrime(f[0]):
    primes.append(f[0])
  dzz = dzielniki(f[0])
  if len(dzzz) < len(dzz):
    dzzz = dzz
    ndz = f[0]
  

  if f[1][::-1] == f[1]:
    if len(palindrom) < len(f[1][::-1]):
      palindrom = f[1][::-1]
  
  
  
file_ans = open('wyniki.txt','w')
print('#1',file=file_ans)
print(f"{len(primes)}%",file=file_ans)
print(primes[-1],file=file_ans)
print('#2',file=file_ans)
print(len(dzzz),file=file_ans)
print(dzzz,file=file_ans) 
print('#3',file=file_ans)
print(palindrom,file=file_ans)
print(len(palindrom),file=file_ans)
print('#4',file=file_ans)
print(sum(data)//len(data),file=file_ans)
data.sort()
print((data[49]+data[50])/2,file=file_ans)


file_ans.close()