edad = input("Edad ")


while (edad.isdigit()==False):

    print("intruduce un numero")
    
    edad = input("Edad ")

if (int(edad)< 18):

    print("No puede pasar")

else:
    print("puede pasar")
