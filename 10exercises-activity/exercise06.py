#exercise 3.16
print("El bono del profesor con base a su puntuacion")
puntuacion=int(input("Ingrese puntos: "))
if puntuacion>=0 and puntuacion<=100:
   print("Salario minimo que recibira de bono sera: 1")
elif puntuacion>=101 and puntuacion<=150:
   print("Salario minimo que recibira de bono sera: 2")
elif puntuacion>=151:
   print("Salario minimo que recibira de bono sera: 3")
