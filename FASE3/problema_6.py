#Anderson Javier Hurtado Moreno
#grupo: 213022B_2201
#APLICACION PIZZA PROBLEMA 6
#areglo matriz 
pizzas = [
    ["Pequeña", 2, 10000],
    ["Mediana", 4, 15000],
    ["Larga", 6, 20000],
    ["Familiar", 8, 25000],
    ["Extra Familiar", 12, 35000]
]

cantidad_vendida = [0, 0, 0, 0, 0]
valor_total_ventas = 0
total_porciones = 0

num_clientes = int(input("Ingrese la cantidad de clientes: "))

for cliente in range(num_clientes):
    print("\nCliente", cliente + 1)
    total_cliente = 0

    tipo = -1
    while tipo != 0:
        print("\nMenu de pizzas")
        for i in range(5):
            print(i + 1, pizzas[i][0], "-", pizzas[i][1], "porciones - $", pizzas[i][2])
        print("0. Finalizar orden")

        tipo = int(input("Seleccione el tipo de pizza: "))

        if 1 <= tipo <= 5:
            indice = tipo - 1
            cantidad_vendida[indice] += 1
            total_cliente += pizzas[indice][2]
            total_porciones += pizzas[indice][1]
            print("Agregada:", pizzas[indice][0])

        elif tipo == 0:
            print("Orden finalizada")
        else:
            print("Opcion no valida")

    valor_total_ventas += total_cliente
    print("Total del cliente: $", total_cliente)

print("\nResumen final")
for i in range(5):
    print(pizzas[i][0], ":", cantidad_vendida[i], "vendidas")

print("Valor total de ventas: $", valor_total_ventas)
print("Total de porciones vendidas:", total_porciones)




    


 