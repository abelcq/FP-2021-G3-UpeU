fun main() {
  //Definir Variables y otros
   println("Ejercicio 01:Area de un Triangulo")
   var b: Int?
   var h: Int?
   var area: Int?
   //Datos de entrada
   println("Ingrese Base:")
   b=readLine()?.toIntOrNull()!!
   println("Ingrese Altura:")
   h=readLine()?.toIntOrNull()!!
   //Proceso
   area=(b*h)/2
   //Datos de salida
   println("El area del triangulo es:"+area)


}

   
