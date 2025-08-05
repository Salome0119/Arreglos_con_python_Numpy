"""_summary_
   
"""
#region ciclo for recorrido ascendente
print("__________ascendente__________")
for i in range(1,11):
    print(i)
#endregion

#region ciclo for recorrido descendentes
print("__________descendente__________")

for i in range(10,0,-1):
    print(i)
#endregion

#region intervalo de 2
print("__________intervalo de 2__________")
for i in range(11,-1,-2):
    print(i)
#endregion

"""_summary_
"""
#region deletrear
#Internamente python lo que hace, la variable hola 
variable = "Hola mundo"
longitud=len(variable)
for i in variable: # variable en esta estructura verifica la longitud
    valor=i
    print("palabra",valor)
#endregion