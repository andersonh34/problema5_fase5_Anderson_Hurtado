"anderson javier hurtado"
"grupo:213022B_2201"
nombre = input("nombre del cliente: ")
print("hola " + nombre )
kwh = float(input("por favor escriba su consumo mensual kwh "))
costo = 320.5
valor_base = kwh * costo
if kwh < 150:
    clacificacion = "bajo"
    descuento = "descuento del 5%"
    total = valor_base * 0.95
elif kwh <=350:
    clacificacion = "medio"
    descuento = "sin ajustye "
    total = valor_base
else:
    clacificacion = "alto"
    descuento = "recargo del 12%"
    total = valor_base * 1.12

print("categoria del consumo: ",clacificacion)  
print("valor base: ",valor_base, "COP")
print("ajuste aplicado: ", descuento)  
print("valor final a pagar: ",total,"COP")

    




 



      