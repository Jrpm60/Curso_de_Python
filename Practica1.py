

# Reto - IVA
# Autor : Jose R. Pablo
# Noviembre 2024

# PROPUESTA

#Un cliente de una empresa de asesoramiento, 
#te han dado una imágen para crear un programa para calcular IVA. 
#Además, necesitan un informe histórico mostrando todos los datos 
#que han introducido los clientes en su calculadora 
#(por ejemplo, Mario hizo un cálculo con 45 euros, Ana hizo con 31 euros, …)

print("\n")
print("CALCULADORA DE IVA")
print("\n")

print ("Sumar IVA")
print (20*"-")
usuario= input("Nombre de Usuario :")
precio_sin_iva = float(input("Precio sin IVA (€):"))
valor_iva = float(input("Valor IVA (%):  "))
print (20*"-")
print("\n")

print("RESULTADO")
print (20*"-")
print(f"Precio sin IVA :, {precio_sin_iva:.2f} €")
print (f"Importe IVA    :, {precio_sin_iva*valor_iva/100:.2f} €")
print(f"Precio con IVA :, {precio_sin_iva+(precio_sin_iva*valor_iva/100):.2f} €")
print (20*"-")
print(3*"\n")

#INFORME MOVIMIENTOS HISTORICOS----------------------------------------

h=input("Pulsa cualquier tecla para ver el historico.")
print("INFORME HISTORICO DE OPERACIONES")
print("\n")
print (60*"-")


historico_usuario=["Carmen", "Pilar", "Maider", "Jon", "Andres"]
historico_importes=[20, 30, 40, 50, 75]
historico_iva=[10, 15, 20, 25, 30]

print("USUARIO:",end=" " )
for usuario in historico_usuario :
    print ("|  ", usuario, end=" ")
print("\n")
print (60*"-")

print("IMPORTE:",end=" " )
for importe in historico_importes :
    print ("|",2*" ",importe, "€", end=" " )
print("\n")
print (60*"-")

print("IVA:    ",end=" " )
for iva in historico_iva :
    print ("|",2*" ",iva, "€", end=" ")
print("\n")
print (60*"-")
