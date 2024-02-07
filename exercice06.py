userInput = 0
inputSums = 0

while inputSums <= 100:
    userInput = int(input("Saisissez un nb entier positif : "))
    inputSums += userInput

    if inputSums > 100:
        print("La somme des nombres dépasse 100. La somme totale est : ", inputSums)
        break

    