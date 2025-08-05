#En python no  es necesario declarar tipo de dato
#reales float double
#float 32 bit, significado de  32 bit que se almacena en 32 bits "reserva de memoria"
#enteros int
#booleanos bool
#string str

"""
   float numero = 3.14
   double numero = 3.1489
   
   tipos de condicionales
   if
   elif
   else
   casos -> match a partir de la version 3.10
   ojo con las versiones de python, por que las versiones inferiores no son compatibles con algunas sintaxis de versiones superiores
   
   ciclo ciclicos => ciclos de repeticion
   for = para
   while = mientras
   break = romper # palabras reserv
   continue = continuar # palabras reservadas en python
   pass = no hacer nada
"""
#condicional simple
if True:
    print("Hola mundo true")
edad = 18
if edad >=18:
    print("Eres mayor de edad")
else:
    print("Eres menor de edad")

#condicionales compuestod
if edad >= 18:
    print("Eres mayor de edad")
else:
    print("Eres menor de edad")
    
#condicionales anidados o multiples
print(" segun el numero es el rol que te va a mostrar")
opcion = int(input("ingrese el numero de opcion: "))
if opcion == 1:
    print("opcion 1 administrador")
if opcion == 2:
    print("opcion 2 usuario")
if opcion == 3:
    print("opcion 3 aprendiz")
else:
    print("opcion no valida")

if opcion==1:
    print("el rol es administrador")
else:
    if opcion==2:
        print("el rol es usuario")
    else:
        if opcion == 3:
            print("el rol es invitado")
        else:
            print("el rol no existe")