#exercise 3.1
def VotoElecciones():
  print("Como saber si puedes votar por tu edad")
  mensaje =""
  edadP=int(input("Ingrese la edad que tiene:"))
  if edadP>=18:
    mensaje ="Usted tiene la edad necesaria para votar"
  else:
    mensaje ="Usted no cumple con la edad mínima para votar"
  print(mensaje)
#VotoElecciones()