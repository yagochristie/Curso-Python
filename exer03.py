salarios =[]

while True:
    salario= float(input('Digite o salario: '))
    if salario==0:
        break
salarios.append(salario)

if salarios[0]> salarios[1]:
     maior= salarios[0]
     segmaior= salarios[1]
else:
     maior = salarios[1]
     segmaior= salarios[0]

for salario in salarios:
        if salario > maior:
            segmaior = maior
            maior = salario
        elif salario> segmaior:
             segmaior = salario
             

print(salarios)
print(maior)
print(segmaior)