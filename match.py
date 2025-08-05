print("segun el numero es el rol que te va a mostrar ")
opcion = int(input("Ingrese el numero de opcion: "))

match opcion:
    case 1:
        print("es el rol de administrador")
    case 2:
        print("es el rol de usuario")
    case 3:
        print("es el rol de aprendiz")
    case _:
        print("el rol no existe")