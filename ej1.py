nom=input("Buenas, ¿cuál es tu nombre? ")
dinero=input("¿Cuánto dinero desea invertir? ")
clean_dinero=dinero.replace(".","")
while clean_dinero.isdecimal()==False:
    print("No has introducido un número, vuelve a probar")
    dinero=input("¿Cuánto dinero desea invertir? ")
    clean_dinero=dinero.replace(".","")
dinero=float(dinero)

inte=input("¿Cuánto interés anual te han prometido? ")
clean_inte=inte.replace(".","")

while clean_inte.isdecimal()==False:
    print("No has introducido un interés, vuelve a probar")
    inte=input("¿Cuánto interés anual te han prometido? ")
    clean_inte=inte.replace(".","")
inte=float(inte)

tipo=input("¿Qué tipo de inversión quieres? (compuesta o simple)")
if tipo.lower()=="simple":
    print("Has elegido una inversión simple")
    print("En 3 años obtendrás "+str(dinero+((dinero*inte)/100*3)))
    
elif tipo.lower()=="compuesta":
    print("Has elegido una inversión compuesta")
    print("En 3 años obtendrás "+str(dinero*((1+inte/100)**3)))
else:
    print("No has introducido ninguna opción válida")