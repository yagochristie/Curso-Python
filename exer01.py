s= 0
numerador = 1
denominador = 1

while denominador<=50:
    s= s + numerador / denominador
    numerador= numerador + 2
    denominador = denominador + 1

print(s)