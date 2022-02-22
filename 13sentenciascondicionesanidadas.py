print ("menu de opciones: ")
print ("presionar 1 para convertir de numero a palabra.")
print ("presiona 2 para convertir de parabra a numero")
opcion = int(input("cual es su opcion deseada?"))

if opcion == 1:
    numero = int(input("ingrese el numero a convertir a continuacion..."))
    if numero == 1:
        print("UNO")
    elif numero == 2:
        print("DOS")
    elif numero == 3:
        print("TRES")
    elif numero == 4:
        print("CUATRO")
    elif numero == 5:
        print("CINCO")
    elif numero == 6:
        print("SEIS")
    elif numero == 7:
        print("SIETE")
    elif numero == 8:
        print("OCHO")
    elif numero == 9:
        print("NUEVE")
    else:
        print("el numero no existe o se confundio")

elif opcion == 2:
    palabra = input("escriba el numero a convertir...")
    palabra = palabra.capitalize()
    if palabra == "Uno":
        print("1")
    elif palabra == "DOS":
        print("2")
    elif palabra == "TRES":
        print("3")
    elif palabra == "CUATRO":
        print("4")
    elif palabra == "CINCO":
        print("5")
    elif palabra == "SEIS":
        print("6")
    elif palabra == "SIETE":
        print("7")
    elif palabra == "OCHO":
        print("8")
    elif palabra == "NUEVE":
        print("9")
    else:
        print("te confundiste de palabra")

else:
    print("selecciona bien el numero capo")