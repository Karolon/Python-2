import random as r
random_values  = []
lenght = 10

for i in range(lenght):
  random_values.append(r.randint(-5,8))

random_values = sorted(random_values)
print(random_values)
sum_of = 0
for i in range(lenght):
  sum_of += random_values[i]
print(sum_of/lenght)

median = 0
if lenght%2 == 0:
  median = (random_values[int(lenght/2)] + random_values[int(lenght/2-1)])/2
else:
  median = random_values[lenght/2]
print(median)

values = []
for i in random_values:
 values.append(abs(i))

y=(max(values))
x=lenght
print(values)

for i in range(y, 0,-1):
  for j in range(x):
    if values[j] >= i:
      print('◘ ', end='')
    else:
      print('  ', end='')
  print()