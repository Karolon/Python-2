kłełe = []
podejście = 'FIFO'
def SIZE(x = kłełe):
  return len(x)

def EPMTY(x = kłełe):
  return SIZE(x) == 0

def PUSH(x, pod = podejście):
  global kłełe
  if pod != 'FIFO':
    kłełe = [x] + kłełe
  else:
    kłełe.append(x)
  
def POP(pod = podejście):
  global kłełe
  if kłełe == []:
    print("PUSTA LISTA!")
    return
  if pod == 'FIFO':
    del kłełe[0]
  else:
    del kłełe[-1]
    
def TOP(pod = podejście):
  global kłełe
  if kłełe == []:
    return "PUSTA LISTA!"
  if pod == 'FIFO':
    x =  kłełe[0]
    del kłełe[0]
  else:
    x = kłełe[-1]
    del kłełe[-1]
  return x


PUSH(1)
PUSH(2)
PUSH(1)
print(kłełe)
print(EPMTY())
POP()
print(SIZE())
print(kłełe)
PUSH(5)
PUSH(0)
print(TOP())
print(kłełe)