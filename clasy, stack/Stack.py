
class Stack:
  def __init__(self):
    self.pile = []
    
  def printStack(self):
    print(*self.pile)
  
  def SIZE(self):
    return len(self.pile)

  def EPMTY(self):
    return self.SIZE() == 0

  def PUSH(self, value):
    self.pile.append(value)
    
  def POP(self):
    if not self.EPMTY():
      del self.pile[-1]
    else:
      print('NO MORE ELEMENTS')
      
  def TOP(self):
    if not self.EPMTY():
      return self.pile[-1]
    print('NO MORE ELEMENTS')


class FIFO:
  def __init__(self):
    self.pile = []
    
  def printStack(self):
    print(*self.pile)
  
  def SIZE(self):
    return len(self.pile)

  def EPMTY(self):
    return self.SIZE() == 0

  def PUSH(self, value):
    self.pile.append(value)
    
  def POP(self):
    if not self.EPMTY():
      del self.pile[0]
    else:
      print('NO MORE ELEMENTS')
      
  def TOP(self):
    if not self.EPMTY():
      return self.pile[0]
    print('NO MORE ELEMENTS')
    
class Queue:
  def __init__(self):
    self.pile = []
    
  def printStack(self):
    print(*self.pile)
  
  def SIZE(self):
    return len(self.pile)

  def EPMTY(self):
    return self.SIZE() == 0

  def push_back(self, value):
    self.pile.append(value)
    
  def pop_front(self):
    if not self.EPMTY():
      del self.pile[0]
    else:
      print('NO MORE ELEMENTS')
      
  def front(self):
    if not self.EPMTY():
      return self.pile[0]
    print('NO MORE ELEMENTS')
    
  def back(self):
    if not self.EPMTY():
      return self.pile[-1]
    print('NO MORE ELEMENTS')