#Medición de ejecución
import time
import os
import os,sys

inicio=time.time()
for i in range(5):
    print(i)
fin=time.time()
tiempoFinal=fin-inicio
print("Tiempo de ejecucuión", tiempoFinal)
if sys.platform == "win32":
    os.system('cls')
else:
    os.system('clear')
    
    
#time.sleep(5)#Pausa 5 segundos
#os.system('cls')# Limpia la consola de windows


#Ciclo mientras

inicio= time.time()
contador=0
while contador <= 10:
    print(contador)
    contador +=1 #contador = contador +1
fin=time.time()
tiempoFinal=fin-inicio
print("Tiempo de ejecucuión", tiempoFinal)
"""
   contador = contador +1
   0 = 0 + 1
   1 = 1 + 1
   2 = 2 + 1
   3 = 3 + 1
   4 = 4 + 1...
"""