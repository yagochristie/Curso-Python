lucro_total= 0 
lucro_10 = 0
lucro_10e20 = 0
lucro_20mais = 0

for i in range(300):
    compra= float(input('Digite o preço de compra: '))
    venda= float(input('Digite o preço de venda: '))

    lucro= venda-compra
    porcentagem= (lucro/compra)* 100
    lucro_total = lucro_total + lucro

    if porcentagem == 10:
        lucro_10= lucro_10 + 1
    elif porcentagem >10 and porcentagem <=20:
        lucro_10e20 = lucro_10e20 + 1
    elif porcentagem > 20:
        lucro_20mais = lucro_20mais + 1

    if porcentagem <= 0:
        print("Você não teve lucro.")

print("Lucro total: R$ %.2f" % lucro_total)
print("Mercadorias com lucro de 10%:", lucro_10)
print("Mercadorias com lucro entre 10% e 20%:", lucro_10e20)
print("Mercadorias com lucro acima de 20%:", lucro_20mais)