#brutto -  ubez społeczne - ubez zdrowotne - PPK pracow - zaliczka 

def brutto_netto(brutto,ppk):
  spoleczne = brutto*(0.0976+ 0.015 + 0.0245)
  zdrowotne = (brutto - spoleczne)*0.09
  PPK = 0
  PPK_p = 0
  Koszty_uzyskania = 250
  if ppk:
    PPK = brutto*0.02
    PPK_p = brutto*0.015
    
  podstawa = round(brutto-spoleczne + PPK_p - Koszty_uzyskania, 0)#zaokrąglić
    
  if podstawa < 120000:
    należny = round(podstawa*0.12-300, 0)
  else:
    należny = round(120000*0.12+(podstawa-120000)*0.32-300, 0)

    
  if należny<0:
    należny = 0
    
  netto = round(brutto - spoleczne - zdrowotne - PPK - należny, 2)
  return (netto)

def netto_brutto():
  netto = float(input())
  #netto = brutto -społeczne - zdrowotne - należny
  #netto = (brutto - brutto*(0.0976+ 0.015 + 0.0245)) - (brutto - brutto*(0.0976+ 0.015 + 0.0245))*0.09 - podstawa*0.12-300
  #netto = (1-0.09)*(brutto - brutto*(0.0976+ 0.015 + 0.0245))- (brutto - brutto*(0.0976+ 0.015 + 0.0245)-250)*0.12-300
  #netto = (1-0.09)*(brutto - brutto*(0.0976+ 0.015 + 0.0245))- (brutto - brutto*(0.0976+ 0.015 + 0.0245)*0.12 -(250)*0.12-300
  #netto = (1-0.09-0.12)*(brutto - brutto*(0.0976+ 0.015 + 0.0245)) -(250)*0.12-300
  #netto = 0.79*(1-0.0976- 0.015 - 0.0245)*brutto  -(250)*0.12-300
  #netto = 0.79*(1-0.0976- 0.015 - 0.0245)*brutto  -(250)*0.12-300
  #netto = 0.79*0.8629*brutto - 330
  #(netto + 330)/(0.79*0.8629) = brutto
  brutto = round((netto - 330)/((1-0.09-0.12)*(1-(0.0976+0.015+0.0245))),2)
  print(brutto)
  


def netto_brutto2():
  netto = float(input())
  i = 80000
  brutto = brutto_netto(i,True)
  while netto != brutto:
    if abs(netto - brutto)< 100:
      if brutto > netto:
        i-=0.01
      else:
        i+0.01
    else:
      if brutto > netto:
        i-=1
      else:
        i+=1
  print(i)
  
  
#i = float(input())
#ppk = bool(input('ppk? tak=1 nie = 0'))
#print(brutto_netto(i,True))
netto_brutto()