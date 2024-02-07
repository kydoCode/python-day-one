# Ask user for int inputs

nombre1 = int(input("Saisissez le premier nombre : "))
nombre2 = int(input("Saisissez le premier nombre : "))

if nombre1 == nombre2:
    print("Les nombres sont égaux")
elif nombre1 > nombre2:
    print("Le premier nombre est plus grand")
elif nombre1 < nombre2:
    print("Le deuxième nombre est plus grand")
else:
    print("Les nombres sont différents")