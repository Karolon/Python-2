'''import tkinter as tk

root = tk.Tk()
root.title('Wieża Hanoi')
root.geometry('500x350')
root.minsize(300,200)
root.maxsize(1000,700)

root.mainloop()
'''
    
class Hanoi:
    
  def __init__(self):
    self.hanoi = [[],[],[]]
    for i in range(5):
      self.hanoi[0].append(i+1)
  
    
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
      self.hanoi[v2] = [a] + self.hanoi[v2]
      del self.hanoi[v1][0]
    else:
      print('Nielegalny ruch')
      
  def printHanoi(self):
    print(*self.hanoi, sep='\n')


tower = Hanoi()
tower.printHanoi()
while not True == False:
  tower.move(int(input()), int(input()))
  tower.printHanoi()