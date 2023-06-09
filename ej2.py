print("Bienvenido a la panadería")
nom=input("¿Cuál es tu nombre? ")

barras=input("¿Cuántas barras quieres del dia? ")
while barras.isdecimal()==False:
    print("No has introducido un número, vuelve a probar")
    barras=input("¿Cuántas barras quieres del dia? ")

barras=int(barras)

barras_ayer=input("¿Cuántas barras quieres de ayer? ")
while barras_ayer.isdecimal()==False:
    print("No has introducido un número, vuelve a probar")
    barras_ayer=input("¿Cuántas barras quieres de ayer? ")
barras_ayer=int(barras_ayer)

descuento=(3.99*25)/100
print("El precio total es " + (str(round(barras*3.99+barras_ayer*descuento, 2))))
print("Te has ahorrado "+str(round(barras_ayer*descuento, 2)))
print("Gracias por usar nuestro programa, hasta pronto")