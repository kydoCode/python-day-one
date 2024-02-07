userInput = 0
inputSums = 0

while inputSums <= 100:
    userInput = int(input("Saisissez un nb entier positif : "))
    inputSums += userInput
     
print("La somme des nombres dépasse 100. La somme totale est : ", inputSums)