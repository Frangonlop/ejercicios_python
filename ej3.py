print("Voy a realizar una división")
dividendo=input("Dame el dividendo ")
while dividendo.isdecimal()==False:
    print("No has introducido un número, vuelve a probar")
    dividendo=input("Dame el dividendo ")
dividendo=int(dividendo)

divisor=input("Dame el divisor ")

while divisor.isdecimal()==False:
    print("No has introducido un número, vuelve a probar")
    divisor=input("Dame el divisor ")
divisor=int(divisor)

if divisor==0:
    print("Error, el divisor no puede ser 0, vuelve a probar")
    divisor=int(input("Dame el divisor "))
    
print("La divisón de los números es "+str(dividendo/divisor))

if divisor%2==0:
    print(str(divisor)+" es par")
else:
    print(str(divisor)+" no es par")
    
if dividendo%2==0:
    print(str(dividendo)+" es par")
else:
    print(str(dividendo)+" no es par")
print("Gracias por usar nuestro programa, hasta luego")