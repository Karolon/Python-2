file = open('pary.txt')

data = []
for f in file:
  data.append(f.strip().split())

#4.1
  
def is_prime(n):
  if n in [0,1,2]:
      return False
  for i in range(2,(n//2)+1):
    if n % i == 0:
      return False
  return True

anser = []
for d in data:
  d = int(d[0])
  if d % 2 == 0:
    biggest_difference = [0,0]
    for i in range(2,d):
      if is_prime(i):
        a = d - i
        if is_prime(a):
          if biggest_difference[1]-biggest_difference[0] <= i - a:
            biggest_difference = [min(i,a), max(i,a)]
    anser.append(str(d)+' '+str(biggest_difference[0])+' '+str(biggest_difference[1]))
      
  
file_ans = open('wyniki4.txt', mode='w')
print('4.1', file=file_ans)
for a in anser:
  print(a, file=file_ans)
  
  
#4.2

print('4.2',file=file_ans)
for d in data:
  old_s = d[1][0]
  anser = ['',0]
  amount = 0
  for s in d[1]:
    if old_s == s:
      amount += 1
      if amount > anser[1]:
        anser=[old_s,amount]
    if old_s != s:
      amount = 0
    old_s = s
    if anser[1] == 0:
      anser = [d[1][0],1]
  print(anser[0]*anser[1], anser[1], file=file_ans)
  
  
#4.3
data2 = []
for d in data:
  if int(d[0]) == len(d[1]):
    data2.append(d)
    
print('4.3', file = file_ans)
print(min(data2), file = file_ans)



file_ans.close( 
               