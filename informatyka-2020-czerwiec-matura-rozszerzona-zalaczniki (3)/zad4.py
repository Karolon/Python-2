file = open('pary.txt')

data = []
for f in file:
  data.append(int(f.strip().split()[0]))
  
def is_prime(n):
  if n in [0,1,2]:
      return False
  for i in range(2,(n//2)+1):
    if n % i == 0:
      return False
  return True

anser = []
for d in data:
  if d % 2 == 0:
    biggest_difference = [0,0]
    for i in range(2,d):
      if is_prime(i):
        a = d - i
        if is_prime(a):
          if biggest_difference[1]-biggest_difference[0] <= i - a:
            biggest_difference = [min(i,a), max(i,a)]
    anser.append(str(d)+' '+str(biggest_difference[0])+' '+str(biggest_difference[1]))
      
  
file_ans = open('zad4.txt', mode='w')
for a in anser:
  print(a, file=file_ans)
  
file_ans.close()