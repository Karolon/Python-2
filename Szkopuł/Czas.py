number = int(input())
time=''
time+= str(number//3600)+'g'
number-=(number//3600)*3600
time+= str(number//60)+'m'
number-=(number//60)*60
time+= str(number)+'s'
print(time)