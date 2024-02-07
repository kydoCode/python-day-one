# startValue = int(input("Saisissez le nombre de départ : "))
endValue = int(input("Saisissez la valeur d'arrêt : "))
# stepValue = int(input("Saisissez une valeur de step : "))
endValueIncrement = endValue + 1
totalSum = 0

for i in range(1, endValueIncrement, 1):
    totalSum += i
    print(totalSum)