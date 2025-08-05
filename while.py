#Formas de controlar while

"""
   Para estudiar
   identificadores o tipos de datos primitivos
   Por numeros sea reales o enteros
   por booleanos
   por cadenas de texto
   
   no primitivos
   listas
   tuplas
   diccionarios
   sets
   rangos
   arreglos : vectores, matrices
   
"""
#region control letra
palabra=input("ingrese una palabra: ")
while palabra.lower()=="S":
   palabra=input("ingrese una palabra:")
print("Fin del ciclo while")
#endregion

#region control False o True
 
contador = 0
while True:
    if contador==10:
        break
        print(contador)
    else:
        print("El contador no ha llegado a 10")
    contador+=1
    
print("El ciclo while ha terminado correctamente")
contador+=1
#endregion
         
