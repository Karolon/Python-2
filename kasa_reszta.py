price = round(float(input('Podaj cenę\n').replace( ',' , '.' ))*100)
cash = round(float(input('Podaj pieniądze\n').replace( ',' , '.' ))*100)
change = cash - price
coins = [500, 200, 100, 50, 20, 10, 5, 2, 1]
coins_amount = [0] * 9 #9 is lenght of coins list
output = ''

i=0
if change < 0:
  output = 'Niewystarczająco pieniędzy'
elif change == 0:
  output = 'Brak reszty'
else:
  print(f"Reszta wynosi: {change / 100 :.2f} zł".replace('.',','))
  while change > 0:
    if coins[i] <= change:
      change -= coins[i]
      coins_amount[i] += 1
    else:
      i += 1
      
if not output:
  for i in range(9): #9 is lenght of coins list
    m = coins[i]
    amount = coins_amount[i]
    if m % 100 == 0:
      if amount == 1:      
        output += f"{m // 100} zł \n"
      elif amount != 0:    
        output += f"{m // 100} zł x {amount} \n"
    else:
      if amount == 1:      
        output += f"{m} gr \n"
      elif amount != 0:    
        output += f"{m} gr x {amount} \n"
    
print(output)