import Stack as s

s1 = s.Stack()
s2 = s.Stack()
s1.printStack()


s1_or = s1
for i in range(5):
  s1.PUSH(i+1)
  
  
for i in range(s1.SIZE()-1):
  s2.PUSH(s1.TOP())
  s1.POP()
  
print(s1.TOP())

s1.POP()
for i in range(s2.SIZE()):
  s1.PUSH(s2.TOP())
  s2.POP()
  
s1.printStack()
  