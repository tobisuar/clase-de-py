import pickle

ficheroapertura = open("losCoches","rb")

misCoches=pickle.load(ficheroapertura)

ficheroapertura.close()

for c in misCoches:
    print(c.estado())
#no funciona al no tener el objeto de coche ni estado