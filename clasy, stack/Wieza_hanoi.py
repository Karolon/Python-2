'''import tkinter as tk

root = tk.Tk()
root.title('Wieża Hanoi')
root.geometry('500x350')
root.minsize(300,200)
root.maxsize(1000,700)

root.mainloop()
'''
    
import Stack as s    


class Hanoi:
    
  def __init__(self, size):
    self.hanoi = [s.Stack(),s.Stack(),s.Stack()]
    for i in range(size):
      self.hanoi[0].PUSH(i+1)
  
    
  def move(self, v1, v2):
    v1 = v1-1
    v2 = v2-1
    
    try:
      a = self.hanoi[v1][0]
    except:
      a = -1
      
    try:
      b = self.hanoi[v2][0]
    except:
      b = -1
      
    if (b == -1 or a < b) and a != -1:
      self.hanoi[v2].PUSH(a)
      self.hanoi[v1].POP()
    else:
      print('Nielegalny ruch')
      
  def printHanoi(self):
    printer = self.hanoi[0].printStack(), self.hanoi[1].printStack(), self.hanoi[2].printStack()
    hight = max(self.hanoi[0].SIZE(), self.hanoi[1].SIZE(), self.hanoi[2].SIZE())
    for i in range(hight):
      for d in printer:
        if d:
          if len(d) < i:
            print('   ', end='')
          else:
            print(str(d[len(d)-i]) + ' '*(3-len(str(d[len(d)-i]))), end='')
        else:
          print('   ', end='')
        print()

  def win(self):
    return self.hanoi[0] == [] and (self.hanoi[1] == [] or self.hanoi[2] == [])



size = int(input('Podaj rozmiar'))
tower = Hanoi(size)
tower.printHanoi()
while not tower.win():
  tower.move(int(input()), int(input()))
  tower.printHanoi()