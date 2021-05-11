-#exercise 3.4
x=int(input("Ingrese horas de uso del estacionamiento: ")) 
if x>0 and x<=2:
   Pagara=x*5
elif x>2 and x<=5:
   Pagara=2*5+(x-2)*4
elif x>5 and x<=10:
   Pagara=2*5+3*4+(x-5)*3
else:
   Pagara=2*5+3*4+5*3+(x-10)*0.20
print("El costo a cobrar es:", Pagara)
