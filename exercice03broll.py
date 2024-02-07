startValue = int(input("Saisissez le nombre de départ : "))
endValue = int(input("Saisissez la valeur d'arrêt : "))
stepValue = int(input("Saisissez une valeur de step : "))
endValueIncrement = endValue + stepValue

for i in range(startValue, endValueIncrement, stepValue):
    print(i)