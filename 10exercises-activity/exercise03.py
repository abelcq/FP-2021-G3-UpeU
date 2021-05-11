#exercise 3.13
def ViajeDeEstudios():
  print("Costo del pasaje de cada alumno")
  CantidadDeAlumnos=int(input("Ingrese la CantidadDeAlumnos: "))
  if CantidadDeAlumnos>100:
    print("El costo del pasaje de cada alumno sera de $20")
  elif 50<=CantidadDeAlumnos<=100:
    print("El costo del pasaje de cada alumno sera de $35")
  elif 20<=CantidadDeAlumnoss<=49:
    print("El costo del pasaje de cada alumno sera de $40")
  elif CantidadDeAlumnos<20:
    print("El costo del pasaje de cada alumno sera de $70")
ViajeDeEstudios()