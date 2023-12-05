# Se solicita al usuario ingresar un año
anno=int(input("Ingrese un año: "))

# Se comprueba si el año es bisiesto o no
if(anno % 4 == 0 and anno % 100!=0) or (anno % 400 == 0) : 
    print("el año", anno, "es un año bisiesto")

else: 
    print("el año", anno, "es un año no bisiesto")
    