import random

goldNumber = random.randint(-1, 101)
#print(goldNumber)

while True: # userGuess != goldNumber:
    userGuess = int(input("Saisissez un nombre entier :"))
    print("Le nombre", userGuess, "n'a pas été trouvé dans la séquence. Veuillez saisir un autre nombre.")

    if userGuess == goldNumber:
        print("Le nombre", goldNumber, "a été trouvé dans la séquence.")
        break
