#Anderson Javier Hurtado Moreno
#grupo: 213022B_2201
#TEMPERATURA HORNO PROBLEMA 1
#areglo matriz 

def pedir_temperatura():
    while True:
        try:
            temp = int(input("Ingrese la temperatura en °C: "))
            if temp < 0:
                print("Error: la temperatura debe ser un número positivo.\n")
            else:
                return temp
        except:
            print("Error: debe ingresar un número entero.\n")

def evaluar_temperatura(temp):
    if temp > 200:
        print("🔴 Alerta: enfriamiento\n")
    elif temp < 180:
        print("🟠 Alerta: calentamiento\n")
    else:
        print("🟢 Temperatura óptima\n")

def preguntar_continuar():
    while True:
        try:
            opcion = int(input("¿Desea continuar? (1: Sí / 0: No): "))
            if opcion in (0, 1):
                return opcion
            else:
                print("Error: ingrese 1 o 0.\n")
        except:
            print("Error: debe ingresar un número.\n")
continuar = 1

while continuar == 1:
    temperatura = pedir_temperatura()
    evaluar_temperatura(temperatura)
    continuar = preguntar_continuar()

print("\nMonitoreo finalizado. ¡Gracias!")

