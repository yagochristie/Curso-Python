sim = 0
nao = 0
fem_sim = 0
mas_nao = 0

for i in range(0, 2000):

    sexo = input("Qual é sua sexualidade, M - masculino \t F - feminino? ")
    resposta = input("Gostou do novo produto? S ou N: ")

    sexo = sexo.upper()
    resposta = resposta.upper()

    if resposta == 'S':
        sim = sim + 1
        if sexo == 'F':
            fem_sim = fem_sim + 1
    elif resposta == 'N':
        nao = nao + 1
        if sexo == 'M:':
            mas_nao= mas_nao + 1

print("Responderam sim:", sim)
print("Responderam não:", nao)
print("Mulheres que responderam sim:", fem_sim)
print("Homens que responderam não:", mas_nao)