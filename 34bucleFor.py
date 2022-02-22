arroba = False
com = False

mail = input ("ingrese un mail")

for i in (mail):
    if (i == "@" or i == "."):
        arroba = True
        com = True

if arroba == True and com == True:
    print("el Email es Correcto ")
