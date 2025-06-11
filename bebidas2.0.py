import os

pedido = []

while True:
    os.system("cls")
    opcion = 0
    
    print("== BEBIDAS 2.0 ==")
    print("1. PEPSI     $900")
    print("2. COCA-COLA $1000")
    print("3. FANTA     $1100")

    opcion = int(input("Ingresa una de las opciones disponibles > "))

    if opcion == 1:
        pedido.append("PEPSI...........$900")
    elif opcion == 2:
        pedido.append("COCA-COLA......$1000")
    elif opcion == 3:
        pedido.append("FANTA..........$1100")
    else:
        input("opción no válida, presione enter para continuar > ")

    salir = int(input("Desea seguir comprando. 1:SI 2:NO > "))
    if salir == 2:
        break

print("==== BOLETA ====")
for p in pedido:
    print(p)