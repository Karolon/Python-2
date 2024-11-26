'''#1
print(int(input())-int(input()))
#2'''
lambda n = int(input()) : print(n//7, '#', n%7, sep='')
#3
x = lambda a, b: a if abs(a)<abs(b) else b
print(x(int(input()),int(input())))
#
#print('tak') if int(input())
