# Matriz de pizzas:
pizzas = [
    ["Pequeña", 2, 10000, 0],
    ["Mediana", 4, 15000, 0],
    ["Larga", 6, 20000, 0],
    ["Familiar", 8, 25000, 0],
    ["Extra Familiar", 12, 35000, 0]
]

valor_total_ventas = 0
total_porciones_vendidas = 0

print("APLICACION VENTA DE PIZZAS")
print()

num_clientes = int(input("Ingrese la cantidad de clientes: "))

for cliente in range(1, num_clientes + 1):
    print("\nCLIENTE", cliente)

    print("Menu de pizzas:")
    for i in range(5):
        print(i + 1, "-", pizzas[i][0], "-", pizzas[i][1], "porciones - $", pizzas[i][2])
    print("0 - Finalizar orden")

    total_cliente = 0
    porciones_cliente = 0
    tipo = -1

    while tipo != 0:
        tipo = int(input("Seleccione el tipo de pizza (1-5) o 0 para terminar: "))

        if 1 <= tipo <= 5:
            indice = tipo - 1

            # Aumentar cantidad vendida
            pizzas[indice][3] += 1

            # Acumular valores
            total_cliente += pizzas[indice][2]
            porciones_cliente += pizzas[indice][1]
            total_porciones_vendidas += pizzas[indice][1]

            print("Agregada:", pizzas[indice][0], "- Precio: $", pizzas[indice][2])

        elif tipo == 0:
            print("Orden finalizada.")
        else:
            print("Opcion no valida.")

    valor_total_ventas += total_cliente

    print("Total a pagar del cliente: $", total_cliente)
    print("Total de porciones del cliente:", porciones_cliente)

print("\nRESUMEN FINAL DE VENTAS")
print("------------------------")

total_pizzas_vendidas = 0
for i in range(5):
    print("Tipo", i + 1, "-", pizzas[i][0], ":", pizzas[i][3], "vendidas")
    total_pizzas_vendidas += pizzas[i][3]

print("\nCantidad total de pizzas vendidas:", total_pizzas_vendidas)
print("Precio total de las pizzas vendidas: $", valor_total_ventas)
print("Numero total de porciones vendidas:", total_porciones_vendidas)





    


 