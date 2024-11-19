
#1

n = int(input())

def ileBlok(n):
  b = 0
  old = -1
  i = 0
  last = 0
  while n:
    last = n%2
    if old != last:
      b += 1
    n = n//2
    old = last
  return b
print(n)




#2

file_ans = open('wyniki2.txt', 'w')

def ileBlokBin(n):
  b = 0
  old = -1
  i = 0
  last = 0
  while n:
    last = n%10
    if old != last:
      b += 1
    n = n//10
    old = last
  return b
print(n, file=file_ans)


data = []
file = open("bin.txt")
amount = 0
for f in file:
  f = int(f.strip())
  data.append(f)
  if ileBlokBin(f) <= 2:
    amount+=1
print(amount, file=file_ans)

#3

print(max(data), file=file_ans)

#4
a = int(input())
b = bin(int(input(),16))[2:]
a = bin(a)[2:]
aswer = ''
for i in range(len(a)):
  if a[-i]==b[-i]:
    aswer += '0'
  else:
    aswer += '1'
print(int(aswer,2))

#odp:14



file_ans.close()