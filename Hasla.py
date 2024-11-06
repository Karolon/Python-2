import random as r

password = ''
length = r.randint(8,32)
for i in range(length):
  password += chr(r.randint(32,122))

specials = list(range(32,48))+list(range(58,65))+list(range(91,97))
password = list(password)
while not([chr(i) for i in specials if chr(i) in password] and [chr(i) for i in range(48,58) if chr(i) in password] and [chr(i) for i in range(65,91) if chr(i) in password] and [chr(i) for i in range(97,122) if chr(i) in password]):
  if not [chr(i) for i in specials if chr(i) in password]:
    password[r.randint(0,length-1)] = chr(specials[r.randint(0,len(specials)-1)])
  if not [chr(i) for i in range(48,58) if chr(i) in password]:
    password[r.randint(0,length-1)] = chr(r.randint(48,57))
  if not [chr(i) for i in range(65,91) if chr(i) in password]:
    password[r.randint(0,length-1)] = chr(r.randint(65,90))
  if not [chr(i) for i in range(97,123) if chr(i) in password]:
    password[r.randint(0,length-1)] = chr(r.randint(97,122))
    
password = ''.join(password)
print(password)