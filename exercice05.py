lineAmount = int(input("Saisissez le nb de lignes souhaité : "))
someStar = "*"
someSpace = " "
# figureDisplay = someStar + someSpace + someStar
spaceIndex = 1

for i in range(lineAmount):
   print("{}{}{}".format(someStar, someSpace, someStar))
   spaceIndex += 2
   someSpace += " " * spaceIndex

