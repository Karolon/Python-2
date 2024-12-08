import tkinter as tk

root = tk.Tk()
root.title('Wieża Hanoi')
root.geometry('500x350')
root.minsize(300,200)


import Stack as s    


class Hanoi:
    
  def __init__(self):
    self.hanoi = [s.Stack(),s.Stack(),s.Stack()]
  
    
  def move(self, v1, v2):
    v1 = v1
    v2 = v2
    
    if v1 == v2:
      return True

    a = self.hanoi[v1].TOP()

      
    b = self.hanoi[v2].TOP()
    if not b:
      b = -1

      
    if (b == -1 or a < b) and a != -1:
      self.hanoi[v2].PUSH(a)
      self.hanoi[v1].POP()
      return True
    else:
      return False
    
  def return_Tower(self):
      return self.hanoi

  def win(self):
    return self.hanoi[0].TOP() == None and (self.hanoi[1].TOP() == None or self.hanoi[2].TOP() == None)

size = ''
input_label = tk.Label(root, text = "Podaj rozmiar wieży")
input_label.place(x = 10, y = 10)
size_setter = tk.Entry(root, width = 10, textvariable=size)
size_setter.place(x = 10, y = 30)

def set_size():
  global size
  size = size_setter.get()
  
input_button = tk.Button(root, command=set_size, text = 'Zatwierdź')
input_button.place(x = 10, y = 50)


while not size:
  root.update()
size = int(size)
root.geometry(f'{size*35}x{size*19}')

input_label.place_forget()
size_setter.place_forget()
input_button.place_forget()
root.update()



root.rowconfigure(0, weight=1)
root.rowconfigure(size+2, weight=1)
root.rowconfigure(size+3, weight=1)


segments = []
for x in range(3):
  root.columnconfigure(x, weight=1)
  segment = []
  for y in range(size):
    root.rowconfigure(y+1, weight=2)
    box = tk.Label(root, text='I', font=50)
    box.grid(column=x, row=y+1)
    segment.append(box)
  segments.append(segment)

count = 0
counter = tk.Label(text=str(count))
counter.grid(row=0,column=2)

tower = Hanoi()

for y in range(size):
  board = tower.return_Tower()
  board[0].PUSH(size - y)
  segments[0][y].config(text='█'*(y+1))
  
  
aired = tk.Label(root, text='', font=50)
aired.grid(column=1, row=0)
move = 3
up = None

def update_window(but):
  global up, tower, move, count
  board = tower.return_Tower()
  height = size - board[but].SIZE()
  if not up:
    up = board[but].TOP()
    if up != None:
      move = but
      segments[but][height].config(text='I')
      aired.config(text='█'*up)
  elif tower.move(move, but):
    if move == but:
      height+=1
    segments[but][height-1].config(text='█'*up)
    aired.config(text=str(up))
    up = None
    count += 1
    counter.config(text=str(count))
  
  root.update()
  
  
def but1():
  update_window(0)
def but2():
  update_window(1)
def but3():
  update_window(2)
  
button1 = tk.Button(root, text=' 1 ', command = but1)
button1.grid(column=0, row=size+2)
button2 = tk.Button(root, text=' 2 ', command = but2)
button2.grid(column=1, row=size+2)
button3 = tk.Button(root, text=' 3 ', command = but3)
button3.grid(column=2, row=size+2)

  

while not tower.win():
  root.update()
  #tower.move(int(input()), int(input()))

  

aired.config(text = '!!! 🎉 WYGRAŁEŚ 🎊 !!!')
button1.grid_forget()
button2.grid_forget()
button3.grid_forget()
  
root.mainloop()