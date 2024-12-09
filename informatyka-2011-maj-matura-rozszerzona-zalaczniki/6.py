file = open("Dane\\liczby.txt")
file_ans = open('zadanie6.txt', 'w')

amount = 0
suma = 0
parzyste = 0
biggest = '0'
for f in file:
  f = f.strip()
  if f [-1] == '0':
    parzyste += 1
  if int(f,2) > int(biggest,2):
    biggest = f
  if len(f) == 9:
    suma += int(f,2)
    amount += 1
    
  
print('a', file=file_ans)
print(parzyste, file=file_ans)
print('b', file=file_ans)
print(biggest, file=file_ans)
print(int(biggest,2), file=file_ans)
print('c', file=file_ans)
print(amount, file=file_ans)
print(bin(suma)[2:], file=file_ans)


file_ans.close()